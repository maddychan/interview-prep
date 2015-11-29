#Maddy Chan 11/28/15
#Cracking the Coding Interview #1.2
#Given two strings, write a method that determines if one is a
#permutation of the other
from collections import defaultdict

def permutation(s1:str,s2:str):
    assert type(s1) == str and type(s2) == str, "Input Types must be String"
    store = defaultdict(int)
    if len(s1) != len(s2):
        return False
    #throwing values in 
    for a in s1:
        store[a] += 1
    for a in s2:
        store[a] -=1
        if store[a] < 0:
            return False
    return True



#test cases
print(permutation("hello", "elloh"))
print(permutation("hello", ""))
print(permutation("", ""))
print(permutation("aabb","aaab"))
#print(permutation(1, ""))      #to test assertions
#print(permutation("",1))

