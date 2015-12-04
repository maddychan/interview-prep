#Maddy Chan 12/1/15
#data structures!

#these are just rough starts, not optimized yet and don't have all
#attribute methods yet

class LN:
    def __init__(self,var = 0, nextnode = None):
        self.value = var
        self.nextNode = nextnode

        
        
#list implementation of stack
class stack:

    def __init__(self, initList = []):
        self.stack = initList

    def push(self,var):
        self.stack.append(var)

    def pop(self):
        return self.stack.pop()

    def __str__(self):
        return 'Stack('+', '.join([str(k) for k in self.stack])+')'

    def __repr__(self):
        return 'Stack('+str(self.stack)+')'

    def __len__(self):
        return len(self.stack)

    def __contains__(self,v):
        return v in self.stack

    def __eq__(self,right):
        if type(right) is stack and len(self.stack) == len(right.stack):
            for i in range(len(self.stack)):
                if self.stack[i] != right.stack[i]:
                    return False
            return True
        return False

    

#queue implementations using linked lists
class queue:
    def __init__(self, initList = []):
        self.head = LN()
        self.end = self.head
        self.size = 0
        for a in initList:
            self.size+=1
            self.end.value = a
            self.end.nextNode = LN()
            self.end = self.end.nextNode

    def enqueue(self, var):
        self.size+=1
        self.end.value = var
        self.end.nextNode = LN()
        self.end = self.end.nextNode

    def dequeue(self):
        if self.size == 0:
            return
        self.size-=1
        var = self.head.value
        self.head = self.head.nextNode
        return var

    def __str__(self):
        place = self.head
        answer = "Queue("+str(place.value)
        place = place.nextNode
        while place.nextNode != None:
            answer+= ', '+ str(place.value)
            place = place.nextNode
        answer+=")"
        return answer

    def __repr__(self):
        param = []
        place = self.head
        while place.nextNode != None:
            param.append(place.value)
            place = place.nextNode
        return 'Queue('+str(param)+')'

    def __len__(self):
        return self.size

    def __contains__(self,v):
        place = self.head
        while place.nextNode != None:
            if place.value == v:
                return True
            place = place.nextNode
        return False

    def __eq__(self,right):
        if type(right) is queue and self.size == right.size:
            place1 = self.head
            place2 = right.head
            for i in range(self.size):
                if place1.value != place2.value:
                    return False
                place1 = place1.nextNode
                place2 = place2.nextNode
            return True
        return False
        

class priorityqueue:

    def __init__(self,gt,initList = []):
        self.head = LN()
        self.gt = gt
        for a in initList:
            place = head
            while(place.nextNode != None):
                pass

    def enqueue(self,var):
        pass

    def dequeue(self):
        pass

