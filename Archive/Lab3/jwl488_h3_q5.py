def count_lowercase(s, low, high, counter = 0):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    if low < high:
        x = 0
        if s[low].islower():
            x = 1
        return count_lowercase(s, low + 1, high) + x


def is_number_of_lowercase_even(s, low, high, counter = 0):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    if low < high:
        x = 0
        if s[low].islower():
            x = 1
        return (count_lowercase(s, low + 1, high) + x)%2 == 0


# print(count_lowercase("LLoooLo", 0, 6))
# print(is_number_of_lowercase_even("LLooLo", 0, 5))
'''
Recieve a string, low and high. 

From low and high, increment through the string till reach base case of one string... 
Ex.

Hello
ello
llo
lo = 
o = 1 

Then... 
o - is the first index lower. Check
lo - is the first index lower, check. 
llo. is the first index lower check. 

return... count + count_lowercase(

'''