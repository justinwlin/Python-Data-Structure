def recursive(word, low, high):
    word = word[low:high]
    return ispalindrome(word)

def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])


print(recursive("kayak", 0,5))