def findchange(lst):
    highIndex = len(lst) - 1
    lowIndex = 0
    divideIndex = int((highIndex + lowIndex)/2)

    control = True
    # if(len(lst) == 2):
    #     if(lst[1] == 1):
    #         return 1
    #     else:
    #         return "improper input, there needs to be 0s and 1s"
    # if(len(lst) == 1):
    #     return "Insert a list larger than a size of 1"
    while(control):
        leftValue = lst[divideIndex -1]
        rightValue = lst[divideIndex + 1]

        if(leftValue == 0 and rightValue == 1):
            if(lst[divideIndex] == 0):
                return divideIndex + 1
            else:
                return divideIndex + 0
        elif (leftValue == 1 and rightValue == 1):
            highIndex = divideIndex
            divideIndex = int((lowIndex + highIndex)/2)
        elif(leftValue == 0 and rightValue == 0):
            lowIndex = divideIndex
            divideIndex = int((lowIndex + highIndex)/2)
        if(highIndex == lowIndex):
            control = False
    return "There needs to be 0s and 1s"


input = [0,0,1,1,1,1,1,1,1,1,1,1,1]
print(findchange(input))
input = [0,1,1,1,1,1,1,1,1,1,1,1,1]
print(findchange(input))
input = [1,1,1,1,1,1,1,1,1,1,1,1,1]
print(findchange(input))
input = [0,1]
print(findchange(input))
input = [0,0,1,1]
print(findchange(input))

'''
Initial Settings.
Find the upperBound = lst.length - 1
LowerBound = 0

Then find the divide in between...
    Check Left and Right of the divide.
    if: right and left = 0, 1
        return divide
    if: right and left = 1,1
        high = divide
        divide = low + high / 2
    if right and left = 0,0
        low = divide
        divide = low + high / 2
'''
    