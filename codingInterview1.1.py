#Maddy Chan 11/28/15
#Cracking the Coding Interview #1.1
#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use additional data structures?

from collections import defaultdict


#this is the O(N^2) solution that takes O(1) extra space
def unique(s:str):
    assert type(s) == str, "Input Type must be String"
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True


#this is the O(N) solution that takes O(N) extra space
def unique2(s:str):
    assert type(s) == str, "Input Type must be String"
    store = defaultdict(int)
    for a in s:
        if store[a] == 1:
            return False
        store[a] = 1
    return True



#test cases
print(unique("hello"))
print(unique("helo"))
print(unique(""))
#print(unique(1))       #to test assertion 
print(unique2("hello"))
print(unique2("helo"))
print(unique2(""))
#print(unique2(1))      #to test assertion 
