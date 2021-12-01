from collections.abc import Iterable

'''
To do:
* Add all magic methods
* Maintain parity with SinglyLinkedList
* Add testing/test coverage
'''

class DoublyLinkedList():
    'Implementation of a doubly-linked-list which tracks head, tail, and length'
    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def __repr__(self):
        circular = bool(self.head and self.tail and self.tail.next is self.head)
        return f'<head={self.head}, tail={self.tail}, circular={circular}, nodes={self.__length}>'

    def __str__(self):
        if not self.head:
            return ''

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
        node = DoublyLinkedList.Node(data)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.__length += 1
        self.tail = node

    def extend(self, data):
        'Append (a) new node(s) from iterable'
        if isinstance(data, Iterable):
            for element in data:
                self.append(element)
        else:
            self.append(data)

    def insert(self, data, index=0):
        'Insert a new node with specified data at specified index, 0 by default'
        node = DoublyLinkedList.Node(data)

        if self.head is None:
            if index != 0:
                raise IndexError(f'Cannot index (to {index}) on empty list')
            self.__length += 1
            self.head = self.tail = node
        elif index > self.__length:
            raise IndexError(f'Requested index ({index}) goes past end of list ({self.__length})')
        elif index == 0:
            self.__length += 1
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            current = self.head
            for _ in range(index):
                previous = current
                current = current.next
            self.__length += 1
            node.next = current
            current.prev = node
            previous.next = node
            node.prev = previous

    @property
    def length(self):
        'Managed access to length attribute - read-only'
        return self.__length

    def sort(self, reverse=False):
        'Sort the list in ascending (descending if reverse=True) order in-place'
        ...


    class Node():
        'DoublyLinkedList Node element'
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            if next and not isinstance(next, DoublyLinkedList.Node):
                raise TypeError(f'next requires DoublyLinkedList.Node, got {type(next)}')
            self.next = next
            if prev and not isinstance(prev, DoublyLinkedList.Node):
                raise TypeError(f'prev requires DoublyLinkedList.Node, got {type(prev)}')
            self.prev = prev

        def __repr__(self):
            return f'<data={self.data}, next={self.next}, prev={self.prev}>'

        def __str__(self):
            if self.data is None:
                return '☐'

            next = 'ᐅ…' if self.next else '❎'
            prev = '…ᐊ' if self.prev else '❎'
            return f'{prev}, {self.data}, {next}'
