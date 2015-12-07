#Maddy Chan 12/1/15
#Interview Cake
#Write a function for reversing a linked list. Do it in-place.
#Your function will have one input: the head of the list.
#Your function should return the new head of the list.

from LN import LN, printList

#solution in O(N) time, O(1) space
def reverse(n):
    if n == None or n.nextNode == None:
        return n
    
    currentNode = n
    nextNode = n.nextNode
    nextnext = n.nextNode.nextNode
    currentNode.nextNode = None
    
    #flipping the references to go the other way, ending with the new head node
    while nextnext != None:
        nextNode.nextNode = currentNode
        currentNode = nextNode
        nextNode = nextnext
        nextnext = nextNode.nextNode
        
    nextNode.nextNode = currentNode
    return nextNode



a = LN(1)
b = LN(2)
c = LN(3)

a.nextNode = b
b.nextNode = c

printList(a)
printList(reverse(a))

#I looked at the solution on InterviewCake after doing this, and their
#implementation is simpler to read. Oh well, I'll try harder next time.

'''
    solution from InterviewCake, for my own reference
def reverse(head_of_list):
    current = head_of_list
    previous = None
    next = None
    
    # until we have 'fallen off' the end of the list
    while current:
        
        # copy a pointer to the next element
        # before we overwrite current.next
        next = current.next
        
        # reverse the 'next' pointer
        current.next = previous
        
        # step forward in the list
        previous = current
        current = next
    
    return previous
'''
