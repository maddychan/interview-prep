#Maddy Chan 12/6/15
#Cracking the Coding Interview 2.2
#Implement an algorithm to find the kth to last element of a singly linked list

from LN import LN


def k_to_last(listNode,k: int):
    first,last = listNode, listNode
    for i in range(k-1):
        if last.nextNode == None:
            return None
        last = last.nextNode

    while last.nextNode != None:
        first = first.nextNode
        last = last.nextNode

    return first




a = LN(1)
b = LN(2,a)
c = LN(3,b)
d = LN(4,c)

print(k_to_last(d,3).value)
