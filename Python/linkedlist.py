class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        # Protect length with property
        # Would a descriptor or attribute access interception be better/stronger
        # to protect this from outside changes?
        self.__length = 0

    def __len__(self):
        return self.__length

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
        # End approach 2


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


if __name__ == '__main__':
    # method = ['append', 'insert', 'pop']
    llist = test_method('append')
    index = int(input())
    llist.pop(index)
    print(llist)
