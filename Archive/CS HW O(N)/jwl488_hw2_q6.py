"""
Logic:
lowIndex = 0
highIndex = lastIndex

Check if:
if lowIndex + highIndex < target...
increase the lowIndex...
if the lowIndex + highIndex > target
lower the highindex...

if lowIndex + highIndex == target
return the indexes...

if lowIndex == highIndex
return no answer
"""

def two_sum(srt_lst, target): #Linear Run Time
    lowIndex = 0
    highIndex = len(srt_lst) - 1

    for i in range(len(srt_lst) -1):
        lowList = srt_lst[lowIndex]
        highList = srt_lst[highIndex]

        if(lowList + highList < target):
            lowIndex = lowIndex + 1
        elif(lowList + highList > target):
            highIndex = highIndex - 1
        elif(lowList + highList == target):
            return lowIndex, highIndex
        else:
            return "No Answer"


input = [-2, 7, 11, 15, 20, 21]
target = 26

print(two_sum(input,target))


