import linkedlist


def test_len():
    def sub_test(expected):
        assert len(llist) == expected, f'Should be {expected}'
        assert llist.__len__() == expected, 'Should be {expected}'

    llist = linkedlist.SinglyLinkedList()
    sub_test(0)

    llist.append(1)
    llist.append(2)
    sub_test(2)

    llist.pop()
    sub_test(1)
