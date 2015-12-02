#Maddy Chan 12/1/15
#Interview Cake
#Write a function for reversing a linked list. Do it in-place.
#Your function will have one input: the head of the list.
#Your function should return the new head of the list.


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

#solution in O(N) time, O(1) space
def reverse(n):
    if n == None or n.next == None:
        return n
    
    currentNode = n
    nextNode = n.next
    nextnext = n.next.next
    currentNode.next = None
    
    #flipping the references to go the other way, ending with the new head node
    while nextnext != None:
        nextNode.next = currentNode
        currentNode = nextNode
        nextNode = nextnext
        nextnext = nextNode.next
        
    nextNode.next = currentNode
    return nextNode

def printList(n):
    while n != None:
        print(n.value)
        n = n.next

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c

printList(a)
printList(reverse(a))

#I looked at the solution on InterviewCake after doing this, and their
#implementation is simpler. Oh well, I'll try harder next time. 