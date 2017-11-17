class Empty(Exception):
    pass


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1

    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.is_empty()):
            raise Empty("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)

def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise Empty
    root = bin_tree.root
    return subtree_min_and_max(bin_tree, root)

def subtree_min_and_max(bin_tree, subtree_root):
    if (subtree_root.left is None and subtree_root.right is None):
        return subtree_root.data
    else:
        if subtree_root.left is not None:
            left_sum = subtree_min_and_max(bin_tree, subtree_root.left)
        else:
            left_sum =  subtree_root.data
        if subtree_root.right is not None:
            right_sum = subtree_min_and_max(bin_tree, subtree_root.right)
        else:
            right_sum = subtree_root.data
        if isinstance(right_sum, int) and isinstance(left_sum,int):  # If both of the comparisons are integer...
            if left_sum > right_sum:  # If the left side of the branch is bigger, than, return...
                tuple = (right_sum, left_sum)  # Min, Max
                return tuple
            if right_sum > left_sum:  # If left side is smaller, return...
                tuple = (left_sum, right_sum)  # Min, max
                return tuple
        elif type(left_sum) is not int and type(right_sum) is int:  # If the left side is a tuple.. but right side isn't...
            # Compare the right versus both the min of the tuple and max of the tuple
            minTuple = left_sum[0]
            maxTuple = left_sum[1]

            if right_sum < minTuple:
                newTuple = (right_sum, maxTuple)
            if right_sum > maxTuple:
                newTuple = (minTuple, right_sum)
            return newTuple
        elif type(left_sum) is int and type(right_sum) is not int:  # If the right side is a tuple.. but left side isn't...
            # Compare the left_sum versus both the min of the tuple and max of the tuple
            minTuple = right_sum[0]
            maxTuple = right_sum[1]

            if left_sum < minTuple:
                newTuple = (left_sum, maxTuple)
            if left_sum > maxTuple:
                newTuple = (minTuple, left_sum)
            return newTuple
        else:
            # If both are tuples... compare each min and max...
            leftMin = left_sum[0]
            rightMin = right_sum[0]

            leftMax = left_sum[1]
            rightMax = right_sum[1]

            newMin = 0
            newMax = 0

            if leftMin < rightMin:
                newMin = leftMin
            else:
                newMin = rightMin
            if leftMax > rightMax:
                newMax = leftMax
            else:
                newMax = rightMax
            newTuple = (newMin, newMax)
            return newTuple

add = LinkedBinaryTree.Node(0)
l_ch1 = LinkedBinaryTree.Node(1, add)
r_ch1 = LinkedBinaryTree.Node(3)
l_ch2 = LinkedBinaryTree.Node(2, l_ch1, r_ch1)
l_ch3 = LinkedBinaryTree.Node(5)
r_ch2 = LinkedBinaryTree.Node(6, l_ch3)
root = LinkedBinaryTree.Node(4, l_ch2, r_ch2)
tree = LinkedBinaryTree(root)

print(min_and_max(tree))