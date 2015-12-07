#Maddy Chan 12/6/15
#Cracking the Coding Interview 3.4
#Implement a MyQueue class which implements a queue using two stacks



class MyQueue:
    def __init__(self,initList = []):
        self.stack1 = initList
        self.stack2 = []
        self.size = len(self.stack1)

    def push(self,var):
        self.size+=1
        self.stack1.append(var)

    def pop(self):
        assert self.size != 0, "Queue is empty"
        self.size -= 1
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def __str__(self):
        answer = "Queue"
        temp = list(reversed(self.stack2))
        temp.extend(self.stack1)
        return answer+str(temp)

    def __repr__(self):
        answer = "MyQueue("
        temp = list(reversed(self.stack2)).extend(self.stack1)
        return answer+str(temp)+")"

    def __len__(self):
        return self.size
    

    
