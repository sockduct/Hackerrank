class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)

def mergeLists(head1, head2):
    if head2 is None:
        return head1
    elif head1 is None:
        return head2

    current = head1
    mergee = head2
    prev = None
    while current and mergee:
        if mergee.data <= current.data:
            node = SinglyLinkedListNode(mergee.data)
            if prev:
                prev.next = node
            else:
                head1 = node
            prev = node
            node.next = current
            mergee = mergee.next
        else:
            prev = current
            current = current.next

    while mergee:
        node = SinglyLinkedListNode(mergee.data)
        prev.next = node
        prev = node
        mergee = mergee.next

    return head1


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())
        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())
        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
        print('\n')
