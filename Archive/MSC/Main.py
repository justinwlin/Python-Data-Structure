import collections
import random
from random import randint
import sys

#BINARY ADDING
def add_binary(num1_str, num2_str):
    return bin(int(num1_str,2) + int(num2_str,2))

#RANSOM NOTE CONSTRUCTION
def can_construct(ransom_note, magazine):
    cnt = collections.Counter(ransom_note)
    cnt2 = collections.Counter(magazine)

    '''print(cnt)
    print(cnt2)
    print(cnt - cnt2)'''
    return (cnt - cnt2 == {})

#PERMUTATION CONSTRUCTION
def create_permutation(n):
    list = []
    loop = True

    while loop:
        temp = randint(0, n - 1)
        if temp not in list:
            list.append(temp)
        if len(list) == n:
            loop = False

    return list

#SCRAMBLE WORD
def scramble_word(word):
    #First find the length of the word
    #generate a permutation number by the length of the word
    #take the # from the 0th index of the permutation, get the number, go to that # index in the string, and store that in a string
    returnstr = ""
    loop = True
    while loop:
        lst = create_permutation(len(word))
        for i in range(0, len(lst)):
            returnstr += word[lst[i]: lst[i] + 1]
        if returnstr != word: #This is to double check that the word scrambled isn't the exact same as the word inserted
            loop = False

    return returnstr

#SPACE IT OUT
def spacingWord(word):
    empty = ""
    for letter in word:
        empty = empty + letter + " "
    return empty

#Guess the scrambled word program
def GuessTheWord():

    #READING FROM THE FILE AND RETURNING THE SCRAMBLED WORD
    with open("words_list.txt") as f:
        lines = f.read().splitlines() #THIS RETURNS ALL THE LINES INTO AN ARRAY' lst
        x = random.randint(0, len(lines) - 1) #GENERATES A NUMBER 0 TO THE LENGTH OF THE ARRAY - 1, TO ACCOUNT FOR THE 0.
        #print("Notepad Words:", lines)
        str = (lines[x]) #GETTING THE STR FROM THE INDEX OF THE ARRAY
        originalWord = str
        scrambled = scramble_word(str)
    #----------------------------------------------------------------
    #Control variables
    loop = True
    counter = 0

    while loop:
        #While loop, get an input, and see if the input is right.
        print("Unscramble the word:", spacingWord(scrambled))
        x = input("")
        if x == originalWord:
            print("Yay, you win.")
            loop = False
        if x != originalWord:
            counter = counter + 1
            print("Try again.")
        if counter == 3:
            print("You failed")
            loop = False

def my_range(start, stop, step):
    curr = start
    while (curr < stop):
        yield curr
        curr += step


#===========:
# =====================================
#================MAIN ENTRY POINT================
#================================================

def main(args=None):
    """The main routine."""
   if args is None:
        args = sys.argv[1:]

    print("random note: ", can_construct("aba", "bbbabbb"))
    print("Binary number:", add_binary("11", "1"))

    for i in range(0, 1):
        print("Permutation number: ", create_permutation(5))

    print("Scrambled word: ", scramble_word("RACHEL"))
    print("---------------")
    GuessTheWord()





if __name__ == "__main__":
    main()





