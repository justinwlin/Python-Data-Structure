#Implement recursive method subtree_insert, that recursively inserts key mapped by key rooted by curr_root
def subtree_insert(self, curr_root, key, value = None):
    if curr_root.left is None and curr_root.right is None and curr_root.data < key:
        curr_root.right = 0 #Create a Node with the key
    elif curr_root.left is None and curr_root.right is None and curr_root.data > key:
        curr_root.left = 0 #Create a Node with the key
    elif curr_root.left is None and curr_root.right is not None:
        if key < curr_root.data:
            curr_root.left = 0 #Node of key
        if key > curr_root.data:
            subtree_insert(self, curr_root.right, key, key)
    elif curr_root.right is None and curr_root.left is not None:
        if key > curr_root.data:
            curr_root.right = 0#Node of key
        if key < curr_root.data:
            subtree_insert(self, curr_root.right, key, key)
    else:
        return



'''
If the left and right is both none, check if the key is greater than the curr_root.data:
a) If so, set the right to a Node of the key

If the left and right is both none, check if the key is less than the curr root.data:
a) curr_root.left = key

If left is none and right is not none:
a) if the key is less than the curr_data set the left to the key Node
b) if none: 
- Recursively call on b

vice-versa on the left is not none and right is none
'''

#Iterative method
'''
while loop(true):
    inside the while loop have a cursor initialized
        check if left of cursor, right of cursor, etc.


'''
