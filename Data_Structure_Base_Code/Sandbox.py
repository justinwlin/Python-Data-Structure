'''
Notes for class:
11/8/17

Testing expression Tree

'''

import LinkedBinaryTree


def eval_exp_tree(tree):
    return eval_exp_subtree(tree.root)

def eval_exp_subtree(subtree_root):
    if(subtree_root.left is None) and (subtree_root.right is None):
        return subtree_root.data
    else:
        left_arg = eval_exp_subtree(subtree_root.left)
        right_arg = eval_exp_subtree(subtree_root.right)

        op = subtree_root.data

        if op == '+':
            return left_arg + right_arg
        elif op == '-':
            return left_arg - right_arg
        elif op == '*':
            return left_arg * right_arg
        elif op == '/':
            return left_arg / right_arg
        else:
            raise Exception("Unsupported operation" + str(op))

l_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(3)
r_ch1 = LinkedBinaryTree.LinkedBinaryTree.Node(4)
l_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node('+', l_ch1, r_ch1)
r_ch2 = LinkedBinaryTree.LinkedBinaryTree.Node(2)

root = LinkedBinaryTree.LinkedBinaryTree.Node('*', l_ch2, r_ch2)
tree = LinkedBinaryTree.LinkedBinaryTree(root)

print(eval_exp_tree(tree))

