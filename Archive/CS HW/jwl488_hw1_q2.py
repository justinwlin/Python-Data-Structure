def shift(lst, k, direction = "left"):
    if direction == "left":
        while k > 0:
            lst.append(lst[0])
            lst.pop(0)
            k -= 1
        return lst
    if direction == "right":
        while k > 0:
            lst.insert(0, (lst[len(lst) - 1]))
            lst.pop(len(lst) - 1)
            k -= 1
        return lst

#TESTING CASES
#==================================
print (shift([1,2,3], 1))
print (shift([1,2,3], 1, "right"))