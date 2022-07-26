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
import queue

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None
        self.x = 0
        self.y = 0

    def __lt__(self, other):
        return self.info < other.info if isinstance(other, Node) else NotImplemented

    def __gt__(self, other):
        return self.info > other.info if isinstance(other, Node) else NotImplemented

    def __repr__(self):
        return f'{self.info:3}-<{self.x:3}, {self.y:2}>'

    def __str__(self):
        return f'{self.info}'


class BinaryTour:
  def __init__(self, tree):
    """Prepare an Euler tour template for given tree."""
    self._tree = tree

  def execute(self):
    """Perform the tour and return any result from post visit of root."""
    if self._tree.root:
      return self._tour(self._tree.root, 0, [])    # start the recursion

  def _tour(self, root, d, path):
    if not path:
        # Root node is horizontal offset 0:
        path.append(0)
    if root.left:
      # Using this to calculate horizontal offset from parent:
      path.append(path[-1] - 1)
      self._tour(root.left, d + 1, path)
      path.pop()
    self._hook_invisit(root, d, path)                   # "in visit" for p
    if root.right:
      # Using this to calculate horizontal offset from parent:
      path.append(path[-1] + 1)
      self._tour(root.right, d + 1, path)
      path.pop()

  def _hook_invisit(self, root, d, path):
      root.x = 0 if d == 0 else path[-1]
      root.y = d


def breadthfirst(tree):
    """Generate a breadth-first iteration of the positions of the tree."""
    if not tree.root:
        return

    q = queue.SimpleQueue()
    q.put(tree.root)
    while not q.empty():
        root = q.get()
        yield root

        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)


def topView(root):
    binary_layout = BinaryTour(tree)
    binary_layout.execute()
    level = 0
    elements = [(e, e.x) for e in breadthfirst(tree)]
    elements.sort(key=lambda e: e[1])
    tracker = set()
    for e in elements:
        if e[1] not in tracker:
            print(f'{e[0]} ', end='')
            tracker.add(e[1])



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
