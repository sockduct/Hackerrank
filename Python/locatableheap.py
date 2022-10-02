#
# Heap using min heap implementation
#
# Based on code from Data Structures and Algorithms in Python by Michael T. Goodrich,
# Roberto Tamassia, and Michael H. Goldwasser
#
# To do:
# * Look at Python heapq to create "bottom-up" __init__ option versus current
#   inefficient technique
#

from collections.abc import Container


class Empty(Exception):
    pass


# Note:  Using slots for small performance boost for data structures challenge
#        measuring time elapsed.
class LocatableHeap:
    '''Implementation of a minimum ordered heap.'''
    __slots__ = '_data'

    class Locator:
        '''Provide a way to immediately access arbitrary items within the heap.'''
        __slots__ = 'value', '_index'

        def __init__(self, value, index):
            self.value = value
            self._index = index

        def __lt__(self, other):
            return self.value < other.value

        def __repr__(self):
            return f'<Locator({self.value}@index={self._index})>'

    def __init__(self, data=None):
        self._data = []

        if isinstance(data, Container):
            # Doesn't work - need to wrap each element in a Locator:
            '''
            if not isinstance(data, list):
                data = list(data)
            heapq.heapify(data)
            '''
            for element in data:
                self.add(element)
        elif data:
            # Doesn't work - need to wrap each element in a Locator:
            # self._data = [data]
            self.add(data)
        else:
            self._data = []

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        size = len(self)
        if size == 0:
            descr = 'empty'
        elif size == 1:
            descr = '1 element'
        else:
            descr = f'{size} elements'

        return f'<Heap({descr})>'

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _has_left(self, index):
        return self._left(index) < len(self._data)   # index beyond end of list?

    def _has_right(self, index):
        return self._right(index) < len(self._data)  # index beyond end of list?

    def _swap(self, index1, index2):
        """Swap the elements at indices index1 and index2 of array."""
        self._data[index1], self._data[index2] = self._data[index2], self._data[index1]
        self._data[index1]._index = index1           # reset locator index (post-swap)
        self._data[index2]._index = index2           # reset locator index (post-swap)

    def _upheap(self, index):
        parent = self._parent(index)
        if index > 0 and self._data[index] < self._data[parent]:
            self._swap(index, parent)
            self._upheap(parent)                     # recur at position of parent

    def _downheap(self, index):
        if self._has_left(index):
            left = self._left(index)
            small_child = left                       # although right may be smaller
            if self._has_right(index):
                right = self._right(index)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[index]:
                self._swap(index, small_child)
                self._downheap(small_child)          # recur at position of small child

    def _bubble(self, index):
        if index > 0 and self._data[index] < self._data[self._parent(index)]:
            self._upheap(index)
        else:
            self._downheap(index)

    def is_empty(self):
        return len(self) == 0

    def add(self, value):
        """Add a value to the heap."""
        token = self.Locator(value, len(self._data)) # initiaize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)            # upheap newly added position
        return token

    def update(self, loc, newval):
        """Update the value for the entry identified by Locator loc."""
        index = loc._index
        if not (0 <= index < len(self) and self._data[index] is loc):
            raise ValueError('Invalid locator')
        loc._value = newval
        self._bubble(index)

    def min(self):
        """Return but do not remove minimum value.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        return self._data[0]

    def remove_min(self):
        """Remove and return minimum value.

        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)           # put minimum item at the end
        item = self._data.pop()                      # and remove it from the list;
        self._downheap(0)                            # then fix new root
        return item

    def remove(self, loc):
        """Remove and return the value identified by Locator loc."""
        index = loc._index
        if not (0 <= index < len(self) and self._data[index] is loc):
            raise ValueError('Invalid locator')
        if index == len(self) - 1:                   # item at last position
            self._data.pop()                         # just remove it
        else:
            self._swap(index, len(self) - 1)         # swap item to the last position
            self._data.pop()                         # remove it from the list
            self._bubble(index)                      # fix item displaced by the swap
        return loc.value

def test_heap():
    heap1 = LocatableHeap()
    heap2 = LocatableHeap(5)
    heap3 = LocatableHeap((3, 7))
    heap4 = LocatableHeap([2, 5, 9, 13])
    heap5 = LocatableHeap({5, 15, 22, 31})

    print(f'heap1:  {heap1}')
    print(f'heap2:  {heap2}')
    print(f'heap3:  {heap3}')
    print(f'heap4:  {heap4}')
    print(f'heap5:  {heap5}')

    try:
        heap1.min()
    except Empty as e:
        print(f'Caught error:  {e}')

    try:
        heap1.remove_min()
    except Empty as e:
        print(f'Caught error:  {e}')

if __name__ == '__main__':
    test_heap()
