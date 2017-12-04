import inspect
import sys

class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def preorder(self):
        for node in self.subtree_preorder(self.root):
            yield node

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)

    def get_ith_smallest(self, i):
        root = self.root
        if i > len(self) or i == 0:
            raise IndexError
        else:
            stack = [] * i
            while True:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if i == 1:
                    return root.item.key
                else:
                    i -= 1
                    root = root.right

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)



class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

#===================================
########### Q2 ####################
#===================================
def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for i in range(1, n + 1):
        bst.subtree_insert(i)
    return bst

def add_items(bst, low, high):
    if high == 0:
        return bst
    if low == high:
        bst.subtree_insert(low)
    else:
        mid = (low + high)//2
        bst.subtree_insert(mid)
        if high - low != 1:
            L = add_items(bst ,low, mid - 1)
        R = add_items(bst, mid + 1, high)

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst
#===================================
########### Q3 ####################
#===================================

def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if prefix_lst == []:
        return bst
    x = restore_bst_subtree(bst, prefix_lst, 0)
    return x

# def restore_bst_subtree(bst, lst, index):
#     if index < len(lst):
#         bst.subtree_insert(lst[index])
#         restore_bst_subtree(bst, lst, index + 1)
#     return bst

def restore_bst_subtree(bst, lst, index):
    #INITIALIZES THE STACK
    stack = ArrayStack()

    #SETS BST ROOT NODE AS 0th INDEX IN LST
    node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[index]))
    bst.root = node
    bst.size += 1
    #PUSH ONTO THE STACK THE NODE
    stack.push(bst.root)

    #WHILE LOOP
    while index < len(lst) - 1:
        #INCREMENT by 1 INDEX
        index += 1
        #INCREASES THE SIZE EVERY TIME THE WHILE LOOP RUNS
        bst.size += 1
        #CREATES A TEMP TO NONE
        temp = None

        #While the stack is not empty and while the lst[index] is greater than the stack.top.key value...
        while not stack.is_empty() and lst[index] > stack.top().item.key:
            temp = stack.pop()

        if temp is not None:
            temp.right = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[index]))
            stack.push(temp.right)
        else:
            temp = stack.top()
            temp.left = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[index]))
            stack.push(temp.left)
    return bst

'''
example_preorder_lst = [9, 7, 3, 1, 5, 13, 11, 15]
result = restore_bst(example_preorder_lst)
result_1 = restore_bst([1])
for node in result.inorder(): #CHECKS IF THE INORDER RESULT is 1
    print(node.item.key == 1)
print("All test cases passed for 3.")



result = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
compare = [9, 7, 3, 1, 5, 13, 11, 15]
compare2 = [1, 3, 5, 7, 9, 11, 13, 15]
i = 0
for node in result.inorder():
    print(node.item.key, end="")
    print(node.item.key == compare2[i])
    i += 1


result = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
compare = [9, 7, 3, 1, 5, 13, 11, 15]
i = 0
for node in result.preorder():
    print(node.item.key, end="")
    print(node.item.key == compare[i])
    i += 1


result = restore_bst([])
i = len(result)
print(i == 0)


result = restore_bst([1])
compare = [1]
i = 0
for node in result.inorder():
    print(node.item.key, end="")
    print(node.item.key == 1)
'''

#===================================
########### Q4 ####################
#===================================
def find_min_abs_difference(bst):
    lst = []
    for node in bst.inorder():
        lst.append(node.item.key)
    pause = [abs(a - b) for a, b in zip(lst, lst[1:])]
    return min(pause)


