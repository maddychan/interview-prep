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
        return 'stack('+str(self.stack)+')'

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
            self.enqueue(a)

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
        for i in range(self.size-1):
            place = place.nextNode
            answer+= ', '+ str(place.value)
        answer+=")"
        return answer

    def __repr__(self):
        param = []
        place = self.head
        for i in range(self.size):
            param.append(place.value)
            place = place.nextNode
        return 'queue('+str(param)+')'

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

#priority queue implemented with linked lists

class priorityqueue:

    def __init__(self,initList = [],gt = (lambda x,y: x > y)):
        self.head = LN()
        self.gt = gt
        self.size = 0
        for a in initList:
            self.enqueue(a)
                    
    def enqueue(self,var):
        self.size+=1
        place = self.head
        while place.nextNode != None and self.gt(place.value,var):
            place = place.nextNode
        place.nextNode = LN(place.value,place.nextNode)
        place.value = var

    def dequeue(self):
        if self.size == 0:
            return
        self.size-=1
        var = self.head.value
        self.head = self.head.nextNode
        return var

    def __str__(self):
        place = self.head
        answer = "PriorityQueue("+str(place.value)
        for i in range(1,self.size):
            place = place.nextNode
            answer+= ', '+ str(place.value)
        answer+=")"
        return answer

    def __repr__(self):
        param = []
        place = self.head
        for i in range(self.size):
            param.append(place.value)
            place = place.nextNode
        return 'priorityqueue('+str(param)+')'

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
        if type(right) is priorityqueue and self.size == right.size:
            place1 = self.head
            place2 = right.head
            for i in range(self.size):
                if place1.value != place2.value:
                    return False
                place1 = place1.nextNode
                place2 = place2.nextNode
            return True
        return False

#set implemented with lists. going to modify using a hash graph later
class listset:

    def __init__(self,initList = []):
        self.set = initList

    def insert(self,var):
        if var in self.set:
            return 0
        self.set.append(var)
        return 1

    def remove(self,var):
        try:
            self.set[self.set.index(var)] = self.set[-1]
            self.set.pop()
            return 1
        except ValueError:
            return 0

    def __str__(self):
        return 'ListSet('+', '.join([str(k) for k in self.set])+')'

    def __repr__(self):
        return 'listset('+str(self.set)+')'

    def __len__(self):
        return len(self.set)

    def __contains__(self,v):
        return v in self.set

    def __eq__(self,right):
        if type(right) is listset and len(self.set) == len(right.set):
            for i in range(len(self.set)):
                if self.set[i] not in right.set:
                    return False
            return True
        return False

#TO DO: hash map
    

