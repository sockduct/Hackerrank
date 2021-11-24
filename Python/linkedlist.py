from collections.abc import Iterable

'''
To Do:
* Build out all magic methods
* Add constructor that accepts iterator to initialize linked list
* Consider alternate constructors via classmethod
* Add testing through unittest and/or pytest
* Way to refactor offset & pop to minimize duplicate code since both similar?
'''

class SinglyLinkedList():
    def __eq__(self, other):
        if self.__length != other.__length:
            return False
        return self.__str__() == other.__str__()

    def __ge__(self, other):
        return NotImplemented

    def __gt__(self, other):
        return NotImplemented

    def __init__(self):
        self.head = None
        self.tail = None
        # Protect length with property
        # Would a descriptor or attribute access interception be better/stronger
        # to protect this from outside changes?
        self.__length = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.__length

    def __le__(self, other):
        return NotImplemented

    def __lt__(self, other):
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        same = self.head is self.tail
        return f'<head={self.head}, tail={self.tail}, head==tail={same}, nodes={self.__length}>'

    def __str__(self):
        if not self.head:
            return None

        current = self.head
        res = ''
        while True:
            res += f'{current.data}'
            if not current.next:
                break
            res += ', '
            current = current.next

        return res

    def append(self, data):
        'Append a new node with specified data at the end'
        node = SinglyLinkedList.Node(data)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.__length += 1
        self.tail = node

    def extend(self, data):
        'Append (a) new node(s) from iterable'
        if isinstance(data, Iterable):
            for element in data:
                # No need to increment length - append handles
                self.append(element)
        else:
            self.append(data)

    def insert(self, data, index=0):
        '''
        Insert a new node with specified data at specified index, 0 by default

        Cases:
        Elements | Index | Error
        None     | 0     | No
        None     | not 0 | Yes
        n        | <= n  | No
        n        | > n   | Yes
        '''
        node = SinglyLinkedList.Node(data)

        if self.head is None:  # Empty Linked List
            if index != 0:
                raise IndexError(f'Cannot index (to {index}) on empty list')
            self.__length += 1
            self.head = self.tail = node
        elif index > self.__length:
            raise IndexError(f'Requested index ({index}) goes past end of list ({self.__length})')
        elif index == 0:
            self.__length += 1
            node.next = self.head
            self.head = node
        else:  # Find insertion point:
            current = self.head
            for _ in range(index):
                previous = current
                current = current.next
            self.__length += 1
            node.next = current
            previous.next = node

    @property
    def length(self):
        'Manage access to length attribute - no updating/deleting'
        return self.__length

    def merge(self, other):
        'Merge two already sorted lists in ascending order'
        if not isinstance(other, SinglyLinkedList):
            raise TypeError(f'Expected {self.__class__} got {other.__class__}')

        current = self.head
        mergee = other.head
        '''
        Cases:
        Lists | Empty
        List1   True
        List2   True
        List1   False
        List2   False
        List1   True
        List2   False
        List1   False
        List2   True
        '''
        if mergee is None:
            return
        elif current is None:
            for data in other:
                # No need to handle length, append handles
                self.append(data)
            return

        index = 0
        while current and mergee:
            if mergee.data <= current.data:
                # No need to handle length, append handles
                self.insert(mergee.data, index=index)
                mergee = mergee.next
            else:
                current = current.next
            index += 1
        while mergee:
            self.append(mergee.data)
            mergee = mergee.next
        '''
        Hackerrank Solutions:

        // Pseudocode:
        MergeSorted(Node a, Node b)
            if a is NULL and b is NULL
                return NULL
            if a is NULL
                return b
            if b is NULL
                return a

            Node c // Combined List
            if ((*a).value < (*b).value)
                c = a
                (*c).next = MergeSorted((*a).next, b)
            else
                c=b
                (*c).next = MergeSorted(a, (*b).next)

            return c

        # Tester's code:
        # head1 and head2 are the first node of each linked list
        def mergeLists(head1, head2):
            # get the correct first node and increment the pointer
            if head1.data < head2.data:
                head = head1
                head1 = head1.next
            else:
                head = head2
                head2 = head2.next
            current = head

            # while both of the lists have data
            while head1 and head2:
                # merge the lower value node
                if head1.data < head2.data:
                    current.next = head1
                    head1 = head1.next
                else:
                    current.next = head2
                    head2 = head2.next
                # and update the pointer
                current = current.next

            # if there are nodes remaining in one of the lists,
            # append it to the result
            if head1:
                current.next = head1
            elif head2:
                current.next = head2

            return head
        '''

    def offset(self, index):
        '''
        Return the data at the offset (index) position
        * Nonnegative offsets start from the head (beginning)
        * Negative offsets start from the tail (end)

        Cases:
        Elements | Index    | Error
        None     | any      | Yes
        n        | >= n     | Yes
        n        | < n      | No
        -n       | [-n, -1] | No
        -n       | other    | Yes

        Note:  Python treats "-0" as 0, so -n < 0
        '''
        if self.__length == 0:
            raise IndexError('Cannot index into empty list')
        elif index >= self.__length or index < -self.__length:
            raise IndexError(f'Requested index ({index}) out of range ({self.__length})')
        '''
        Cases:
        index = 0 or -self.__length             == Head
        index = self.__length - 1 or -1         == Tail
        index in range(1, self.__length - 1)    == Middle (left -> right)
        index in range(-1, -self.__length, - 1) == Middle (right -> left)
        '''
        if index in [0, -self.__length]:
            return self.head.data

        if index < 0:
            index = self.__length + index

        offset = 0
        current = self.head
        while offset < index:
            current = current.next
            offset += 1
        return current.data

    def pop(self, index=-1):
        '''
        Remove an existing node and return its value, default index is -1 or the
        end of the list

        Cases:
        Elements | Index    | Error
        None     | any      | Yes
        n        | >= n     | Yes
        n        | < n      | No
        -n       | [-n, -1] | No
        -n       | other    | Yes

        Note:  Python treats "-0" as 0, so -n < 0
        '''
        if self.__length == 0:
            raise IndexError('Cannot pop empty list')
        elif index >= self.__length or index < -self.__length:
            raise IndexError(f'Requested index ({index}) out of range ({self.__length})')

        '''
        Cases:
        index = 0 or -self.__length             == Head
        index = self.__length - 1 or -1         == Tail
        index in range(1, self.__length - 1)    == Middle (left -> right)
        index in range(-1, -self.__length, - 1) == Middle (right -> left)
        '''
        if index in [0, -self.__length]:
            data = self.head.data
            self.head = self.head.next
        else:
            if index < 0:
                index = self.__length + index

            offset = 0
            current = self.head
            while offset < index:
                previous = current
                current = current.next
                offset += 1
            data = current.data
            previous.next = current.next
            if self.tail == current:
                self.tail = previous

        self.__length -= 1
        return data


    def reverse(self):
        'Reverse list in place'
        if self.__length in [0, 1]:
            return
        elif self.__length == 2:
            old_head = self.head
            self.head = self.tail
            self.head.next = old_head
            self.tail = old_head
            self.tail.next = None
            return

        # One approach - stack data into a list and then rewrite the list data
        # in reverse by popping it from the stack
        '''
        current = self.head
        stack = [current.data]
        while current.next:
            current = current.next
            stack.append(current.data)

        current = self.head
        while stack:
            current.data = stack.pop()
            current = current.next
        '''
        # End approach 1


        # Another approach, change pointers by using a 3 node circular queue of
        # SinglyLinkedList.Nodes
        '''
        q = SinglyLinkedList.Circularq(3)
        current = 0
        q[current] = self.head
        q[current + 1] = q[current].next
        self.tail = self.head
        self.tail.next = None
        while q[current + 1].next:
            q[current + 2] = q[current + 1].next
            q[current + 1].next = q[current]
            current += 1
        q[current + 1].next = q[current]
        self.head = q[current + 1]
        '''
        # End approach 2


        # Hackerrank inspired solution - use 3 references/pointers
        prev = None
        current = self.head
        self.tail = self.head
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        # End approach 3
        '''
        Hackerrank Solutions:
        prev = NULL
        cur = head
        nxt = NULL
        while cur is not NULL
            nxt = (*cur).next
            (*cur).next = prev
            prev = cur
            cur = nxt
        head = prev
        return head

        nxt = None
        while head:
            tmp = head.next
            head.next = nxt
            nxt = head
            head = tmp
        return nxt
        '''


    class Node():
        'SinglyLinkedList Node element'
        def __init__(self, data=None, next=None):
            self.data = data
            if next and not isinstance(next, SinglyLinkedList.Node):
                raise TypeError(f'next requires SinglyLinkedList.Node, got {type(next)}')
            self.next = next

        def __repr__(self):
            return f'<data={self.data}, next={self.next}>'

        def __str__(self):
            if self.data is None:
                return '☐'

            # Started with stop sign, but that's hard to deal with because
            # it's outside the BMP and my console program cannot display it!
            more = '➔…' if self.next else '❎'
            return f'{self.data}, {more}'


    class Circularq():
        'Circular queue of SinglyLinkedList Node elements'
        def __getitem__(self, index):
            index %= self.__length
            return self.__data[index]

        def __init__(self, elements):
            if elements < 1:
                raise ValueError(f'{self.__class__} must be instantiated with a '
                                 f'positive number of elements - got {elements}')
            self.__data = [SinglyLinkedList.Node() for _ in range(elements)]
            self.__length = elements

        def __len__(self):
            return self.__length

        def __repr__(self):
            term = '❎' if self.__length == 1 else '2=…'
            return f'<{self.__length} elements, 1={self.__data[0]}, {term}'

        def __setitem__(self, index, value):
            index %= self.__length
            self.__data[index] = value


def test_method(method):
    llist = SinglyLinkedList()
    n = int(input())
    for _ in range(n):
        getattr(llist, method)(int(input()))

    return llist


def test_merge():
    ll1 = SinglyLinkedList()
    ll2 = SinglyLinkedList()

    ll1.extend(range(1, 6))
    ll2.extend(range(3, 15, 2))

    ll1.merge(ll2)
    test_res = ', '.join(map(str, sorted(map(int, ll1.__str__().split(', ')))))
    assert ll1.__str__() == test_res, ("Merge didn't work right.\n     Got:  "
                                       f'{ll1.__str__()},\nExpected:  {test_res}.')


if __name__ == '__main__':
    # method = ['append', 'insert', 'pop']
    '''
    llist = test_method('append')
    index = int(input())
    llist.pop(index)
    print(llist)
    '''
    test_merge()
