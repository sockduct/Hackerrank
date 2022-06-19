#! /usr/bin/env python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(head, data):
    # Write your code here
    # Cases:
    # Empty list => insert_node (special case)
    # Non-empty list:
    # * < 1st (special case)
    # * while
    # * = 1st/current
    # *
    new_list = DoublyLinkedList()
    inserted = False

    # Non-empty list:
    if head:
        current = head
        while current:
            if data < current.data and not inserted:
                new_list.insert_node(data)
                inserted = True

            new_list.insert_node(current.data)

            if not current.next and not inserted:
                # Data >= last node, add to end:
                new_list.insert_node(data)
                inserted = True

            current = current.next
    # Empty List
    else:
        new_list.insert_node(data)

    return new_list.head


if __name__ == '__main__':
    fptr = sys.stdout
    test_cases = int(input())

    for _ in range(test_cases):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')
