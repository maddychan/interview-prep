#Maddy Chan 12/6/15
#Cracking the Coding Interview 3.3
#Set of Stacks - create a stack data structure that makes a new stack when the
#first one passes a certian threshold. Add a popAt(index) method that will let
#you pop from that stack.

#I'm assuming that when you pop from the middle of a stack,
#the stacks should readjust themselves so that the lower stacks are back to capacity

class setOfStacks:
    def __init__(self,threshold = 10, initList = []):
        self.stack = [[]]
        self.threshold = threshold
        self.current = self.stack[0]
        self.size = 0
        for a in initList:
            self.push(a)

    def push(self, var):
        self.size += 1
        if len(self.current) == self.threshold:
            self.stack.append([])
            self.current = self.stack[-1]
        self.current.append(var)

    def pop(self):
        assert self.size != 0, "Stack is empty"
        self.size -= 1
        val = self.current.pop()
        if len(self.current) == 0 and self.size != 0:
            self.stack.pop()
            self.current = self.stack[-1]
        return val

    def popAt(self,index):
        assert index >=0 and index < len(self.stack), "Index out of range"
        val = self.stack[index].pop()
        while index < len(self.stack)-1:
            self.stack[index].append(self.stack[index+1].pop(0))
            index+=1
        if len(self.current) == 0:
            self.stack.pop()
            self.current = self.stack[-1]
        return val

    def __str__(self):
        answer = "Stack["
        for a in self.stack:
            for b in a:
                answer+= str(b) + ", "
        return answer[:-1]+"]"

    def __repr__(self):
        answer = "setOfStacks("+str(self.threshold)+", "
        temp = []
        for a in self.stack:
            temp.extend(a)
        return answer + str(temp) + ")"

    def __len__(self):
        return self.size
    
        
