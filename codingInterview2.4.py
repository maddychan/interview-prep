#Maddy Chan 12/6/15
#Cracking the Coding Interview 2.4
#Write code to partition a linked list around a value x, such that
#all nodes less than x come before all nodes greater or equal to x

from LN import LN, printList

def partition(ln,x: int):
    front,back = None, None
    head = None
    place = ln
    if place.nextNode == None:
        return place
    nextplace = place.nextNode
    while nextplace != None:
        nextplace = place.nextNode
        if place.value < x:
            if front == None:
                front = place
                head = front
            else:
                front.nextNode = place
                front = front.nextNode
        else:
            place.nextNode = back
            back = place
        place = nextplace
    front.nextNode = back
    return head
            
a = LN(3)
b = LN(5,a)
c = LN(9,b)
d = LN(2,c)
e = LN(6,d)
printList(e)
print()
printList(partition(e,6))
    
