def flat_list(lst, low, high, isCtrl = True):
    if isCtrl == True:
        lst = lst[low:high + 1]
        isCtrl = False
    if lst == []:
        return lst
    if isinstance(lst[0], list):
        return flat_list(lst[0], low, high, isCtrl) + flat_list(lst[1:], low, high, isCtrl)
    return lst[:1] + flat_list(lst[1:], low, high, isCtrl)

s = [[1,2], 3, 4, [5,6]]
print(flat_list(s, 2, 3))

# def flat_list(lst, low = 0, high = len(lst) - 1, isTrue = True):
#     if isTrue == True
#         lst = lst[low:high + 1]
#     if lst == []:
#         return lst
#     if isinstance(s[low], list):
#         return flat_list(lst[0], low, high, False) + flat_list(lst[1:], low,high , False)
#     return lst[:1] + flat_list(lst[1:], low, high, False)
#
# s=[[1,2],[3,4], [5,6,4], 1, 3, 4]
# print("flat_listed list is: ",flat_list(s, , high))

'''
Given a list: 
[[1,2], [3,4], 5, 6]]

Check within the range of low and high. 
Ex. 2 and 4. 

[3,4], 5, 6

Return a collapsed list... 
I
if isInstance at low is a list... 
    Return that list through the function, spliced from the others, (A)
        - function(lst[low], low, high]
    run the other half through the function still. function(lst, low + 1, high)(B)
    
(A):
- If it is not a list:
return lst[:1] - the 0th index. 
 + Run the rest of the sublist through with the 0th index, continued to take out. 
    function(lst[1:], low, high)
; If the list becomes empty, return []

(B)
If index at low, is not a list: 
Run: function(lst[1:], low, high)

If it is a list... Then... 


'''