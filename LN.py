#Maddy Chan

#Linked List module

class LN:
    def __init__(self,value = 0, nextNode = None):
        self.value = value
        self.nextNode = nextNode
        
def printList(n):
    while n != None:
        print(n.value)
        n = n.nextNode
