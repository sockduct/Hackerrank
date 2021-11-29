import unittest

import linkedlist


'''
Assert methods:
.assertEqual(a, b)  	a == b
.assertTrue(x)      	bool(x) is True
.assertFalse(x)     	bool(x) is False
.assertIs(a, b)     	a is b
.assertIsNone(x)    	x is None
.assertIn(a, b) 	    a in b
.assertIsInstance(a, b)	isinstance(a, b)
.assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have
 opposite methods, named .assertIsNot(), and so forth.

Are you testing side effects such as altering:
* an attribute of a class
* a file on the filesystem
* a value in a database
'''
class TestSinglyLinkedList(unittest.TestCase):
    def test_len(self):
        def sub_test(expected):
            self.assertEqual(len(llist), expected, f'Should be {expected}')
            self.assertEqual(llist.__len__(), expected, 'Should be {expected}')

        llist = linkedlist.SinglyLinkedList()
        sub_test(0)

        llist.append(1)
        llist.append(2)
        sub_test(2)

        llist.pop()
        sub_test(1)


if __name__ == '__main__':
    unittest.main()
