class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f'<head={self.head}>'

    def __str__(self):
        if self.head:
            current = self.head
            res = ''
            while True:
                res += f'{current.data}'
                if current.next:
                    res += ', '
                    current = current.next
                else:
                    break
        else:
            return None

        return res

    def append(self, data):
        node = SinglyLinkedList.Node(data)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def insert(self, data):
        node = SinglyLinkedList.Node(data)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


    class Node():
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def __repr__(self):
            return f'<data={self.data}, next={self.next}>'

        def __str__(self):
            if self.data:
                # Started with stop sign, but that's hard to deal with because
                # it's outside the BMP and my console program cannot display it!
                more = '➔…' if self.next else '❎'
                return f'{self.data}, {more}'
            else:
                return '☐'


def main():
    pass


if __name__ == '__main__':
    main()
