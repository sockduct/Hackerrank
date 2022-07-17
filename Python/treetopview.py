#! /usr/bin/env python3

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Specifications are unclear - for good description of what's desired see:
# https://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
# Note:  Warning (spoiler alert!) - the above link provides solutions!
#
# Need to do breadth-first-traversal and figure out what's "visible" from the
# "top"
def topView(root):
    def leftTopView(root):
        if root and root.left:
            leftTopView(root.left)

            print(f'{root.info} ', end='')

    def rightTopView(root):
        if root:
            print(f'{root.info} ', end='')

            if root.right:
                rightTopView(root.right)

    leftTopView(root)

    if root:
        print(f'{root.info} ', end='')

        if root.right:
            rightTopView(root.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
