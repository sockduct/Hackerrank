#! /usr/bin/env python3

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_at(self, pos, val):
        if val < pos.info:
            if pos.left:
                self.insert_at(pos.left, val)
            else:
                pos.left = Node(val)
        elif val > pos.info:
            if pos.right:
                self.insert_at(pos.right, val)
            else:
                pos.right = Node(val)
        else:
            raise ValueError(f'Duplicate value "{val}"')

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insert_at(self.root, val)


'''
Test:
# Input
6
4 2 3 1 7 6

# Output
4 2 1 3 7 6
'''
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
