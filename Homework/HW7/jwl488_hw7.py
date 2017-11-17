class EmptyTree(Exception):
    pass


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
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
            raise EmptyTree("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if (subtree_root.left is None) and (subtree_root.right is None):
            return 0
        elif subtree_root.left is None or subtree_root.right is None:
            if subtree_root.left is None:
                return 1 + self.subtree_height(subtree_root.right)
            else:
                return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)

    def preorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    def preorder2(self):
        yield from self.subtree_inorder(self.root)

    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            print(subtree_root)
            self.subtree_preorder(subtree_root.left)
            self.subtree_preorder(subtree_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root

    def iterative_inorder(self):
        current = self.root
        while current is not None:
            if current.left is None:
                yield current.data
                current = current.right
            else:
                pred = current.left
                while pred.right is not None and pred.right != current:
                    pred = pred.right
                if pred.right is None:
                    pred.right = current
                    current = current.left
                else:
                    pred.right = None
                    yield current.data
                    current = current.right

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield node.data

    def leaves_list(self):
        if self.root == None:
            return []
        return self.leaves_list_helper(self.root, [])

    def leaves_list_helper(self, subtree_root, leaves, firstTime = None):
        #EDGE CASE
        if firstTime is None:
            if subtree_root is not None and subtree_root.left is None and subtree_root.right is None:
                return [subtree_root.data]
            else:
                firstTime = False
        #BASE CASE
        if subtree_root.left is None and subtree_root.right is None:
            leaves.append(subtree_root.data)
        if subtree_root.left is not None:
            self.leaves_list_helper(subtree_root.left, leaves, firstTime)
        if subtree_root.right is not None:
            self.leaves_list_helper(subtree_root.right, leaves, firstTime)
        return leaves


def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree
    if bin_tree.root.left is None and bin_tree.root.right is None:
        tup = bin_tree.root.data, bin_tree.root.data
        return tup
    def subtree_min_and_max(bin_tree, subtree_root):
        if (subtree_root.left is None and subtree_root.right is None):
            return subtree_root.data
        else:
            if subtree_root.left is not None:
                left_sum = subtree_min_and_max(bin_tree, subtree_root.left)
                check = subtree_root.data
                if type(left_sum) is int:
                    if check < left_sum:
                        left_sum = (check, left_sum)
                    else:
                        left_sum = (left_sum, check)
                else:
                    if check < left_sum[0]:
                        left_sum = (check, left_sum[1])
                    if check > left_sum[1]:
                        left_sum = (left_sum[0], check)
            else:
                left_sum = subtree_root.data
            if subtree_root.right is not None:
                right_sum = subtree_min_and_max(bin_tree, subtree_root.right)
                check = subtree_root.data

                if type(right_sum) is int:
                    if check < right_sum:
                        right_sum = (check, right_sum)
                    else:
                        right_sum = (right_sum, check)
                else:
                    if check < right_sum[0]:
                        right_sum = (check, right_sum[1])
                    if check > right_sum[1]:
                        right_sum = (right_sum[0], check)
            else:
                right_sum = subtree_root.data
            if isinstance(right_sum, int) and isinstance(left_sum, int):  # If both of the comparisons are integer...
                if left_sum > right_sum:  # If the left side of the branch is bigger, than, return...
                    tuple = (right_sum, left_sum)  # Min, Max
                    return tuple
                if right_sum > left_sum:  # If left side is smaller, return...
                    tuple = (left_sum, right_sum)  # Min, max
                    return tuple
            elif type(left_sum) is not int and type(
                    right_sum) is int:  # If the left side is a tuple.. but right side isn't...
                # Compare the right versus both the min of the tuple and max of the tuple
                minTuple = left_sum[0]
                maxTuple = left_sum[1]

                newTuple = (minTuple, maxTuple)
                if right_sum < minTuple:
                    newTuple = (right_sum, maxTuple)
                if right_sum > maxTuple:
                    newTuple = (minTuple, right_sum)
                return newTuple
            if type(left_sum) is int and type(
                    right_sum) is not int:  # If the right side is a tuple.. but left side isn't...
                # Compare the left_sum versus both the min of the tuple and max of the tuple
                minTuple = right_sum[0]
                maxTuple = right_sum[1]

                newTuple = (minTuple, maxTuple)
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
    root = bin_tree.root
    #HELPER FUNCTION
    return subtree_min_and_max(bin_tree, root)


def is_height_balanced(bin_tree):
    root = bin_tree.root
    return sub_balanced(root) >= 0


def sub_balanced(root):
    if root is None:
        return 0;
    left = sub_balanced(root.left)
    right = sub_balanced(root.right)
    if left < 0 or right < 0 or abs(left - right) > 1:
        return -1
    return max(left, right) + 1


def create_expression_tree(prefix_exp_str):
    lst = prefix_exp_str.split(' ')
    output = subcreate_tree(lst, 0)
    return LinkedBinaryTree(output[0])

def subcreate_tree(lst, index):
    if lst[index].isdigit():
        intVersion = int(lst[index])
        return LinkedBinaryTree.Node(intVersion), 1
    else:
        left = subcreate_tree(lst, index + 1)
        right = subcreate_tree(lst, index + left[1] + 1)
        return LinkedBinaryTree.Node(lst[index], left[0], right[0]), left[1] + right[1] + 1

def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    ouput = []
    for item in tree.postorder():
        ouput.append(str(item.data))
    return ' '.join(ouput)

c=LinkedBinaryTree.Node(5)
d=LinkedBinaryTree.Node(1)
e=LinkedBinaryTree.Node(8,c,d)
f=LinkedBinaryTree.Node(4)
g=LinkedBinaryTree.Node(7,e,f)
h=LinkedBinaryTree.Node(9)
i=LinkedBinaryTree.Node(2,h)
j=LinkedBinaryTree.Node(3,i,g)
treee=LinkedBinaryTree(j)

for i in treee.preorder():
    print (i.data)

for l in treee.preorder2():
    print(l.data)