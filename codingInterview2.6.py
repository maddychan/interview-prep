#Maddy Chan 12/6/15
#Cracking the Coding Interview 2.4
#Implement an algorithm to check if a list is a palindrome

from LN import LN, printList
from math import ceil

#I assume I have the linked list as well as the length

def palindrome(listNode, l: int):
    ln,stack = listNode,[]
    half = ceil(l/2)
    #loading half the nodes into the stack
    for i in range(half):
        stack.append(ln.value)
        ln = ln.nextNode
    #dequeueing if it's an odd number of nodes
    if half%2 == 1:
        stack.pop()
    #checking to see if the second half mirrors the first
    while ln != None:
        if ln.value != stack.pop():
            return False
        ln = ln.nextNode
    return True


a = LN(3)
b = LN(2,a)
c = LN(1,b)
d = LN(2,c)
e = LN(3,d)
f = LN(4,e)

printList(f)
print()
print(palindrome(f,6))
