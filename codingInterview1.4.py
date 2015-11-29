#Maddy Chan 11/28/15
#Cracking the Coding Interview 1.4
#Given a string, write a function that checks if it is a
#permutation of a palindrome
from collections import defaultdict

def palindrome(s:str):
    store = defaultdict(int)
    #adding up how many of each letter is seen
    s = s.lower()
    for a in s:
        if a != " ":
            store[a]+=1
    #one letter is allowed to only occur once in the middle
    middle = False
    #making sure everything else other than that one letter has an even number
    for num in store.values():
        if num == 1:
            if middle:
                return False
            else:
                middle = True
        elif num%2 != 0:
            return False
    return True

print(palindrome("Tact Coa"))
print(palindrome("racecar"))
print(palindrome(""))
print(palindrome("pineapple"))
