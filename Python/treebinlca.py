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
'''
Testing:

# Input:
6
4 2 3 1 7 6
1 7

# Output:
Pointer to node containing 4, the lowest common ancestor of 1 and 7
'''
def find_node(node, target):
    if target == node.info:
        return node
    elif target < node.info:
        return find_node(node.left, target)
    else:
        return find_node(node.right, target)

def get_path(node, target, path=None):
    if not path:
        path = []

    path.append(node.info)
    if target == node.info:
        return path
    elif target < node.info:
        return get_path(node.left, target, path)
    else:
        return get_path(node.right, target, path)

def lca(root, v1, v2):
    v1_path = get_path(root, v1)
    v2_path = get_path(root, v2)

    in_common = list(set(v1_path) & set(v2_path))
    if len(in_common) == 1:
        return find_node(root, in_common[0])

    max_value = -1
    for value in in_common:
        if (cur_value := v1_path.index(value)) > max_value:
            max_value = cur_value

    return find_node(root, v1_path[max_value])

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
