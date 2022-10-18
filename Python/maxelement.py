#! /usr/bin/env python3

'''
Challenge goals:
Start with empty sequence and given N queries:
1) Push the element x into the stack.
2) Delete the element present at the top of the stack.
3) Print the maximum element in the stack.
'''

import avl_tree
# Debug and fix!!!:
# from red_black_tree import RedBlackTree

def getMax(ops):
    stack = []
    tree = avl_tree.AVLtree()
    results = []

    for op in ops:
        choice, *arg = op.split()
        if choice == '1':
            val = int(arg[0])
            stack.append(val)
            tree.insert(val)
        elif choice == '2':
            val = stack.pop()
            tree.del_node(val)
        elif choice == '3':
            results.append(avl_tree.get_right_most(tree.root))
        else:
            raise ValueError(f'Unexpected selection:  {choice}')

        # Debug
        print(f'Stack:  {stack}')
        print(f'Tree:  {tree}')
        print('='*50)

    return results


def main():
    ops = [input() for _ in range(int(input()))]
    results = getMax(ops)
    print(results)


if __name__ == '__main__':
    main()
