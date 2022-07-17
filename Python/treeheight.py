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

# Enter your code here. Read input from STDIN. Print output to STDOUT
def height(root):
    'Return integer denoting height of tree calculuated from passed in tree root'
    depth = []
    level = 0

    # Pre-order tree traversal:
    def preOrder(root):
        nonlocal depth
        nonlocal level

        if root:
            # Examin root.info then children:
            if root.left:
                level += 1
                preOrder(root.left)
            if root.right:
                level += 1
                preOrder(root.right)

            # No more children
            depth.append(level)
            level -= 1

    preOrder(root)
    return max(depth)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
