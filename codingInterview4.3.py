#Maddy Chan 12/7/15
#Cracking the Coding Interview 4.3
#Given a binary tree, design an algorithm which creates a linked list
#of all the nodes at each depth

#I'm going to store each depth in an index of a list, with a header linked list

from TN import TN, printTree
from LN import LN, printList
from codingInterview42 import minimalTree

def listDepth(TN,DL,index):
    if TN != None:
        DL[index].nextNode = LN(TN.value,DL[index].nextNode)
        listDepth(TN.left,DL,index+1)
        listDepth(TN.right,DL,index+1)

l = [1,2,3,4,5,6,7,8,9]
root = minimalTree(l)
print(printTree(root,""))
DL = [LN(),LN(),LN(),LN()]

listDepth(root,DL,0)

for a in DL:
    printList(a.nextNode)
    print()




