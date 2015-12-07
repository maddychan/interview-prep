#Maddy Chan 12/6/15
#Cracking the Coding Interview 2.5
#YOu have two numbers represented by a linked list where each node contains a
#single digit. The digits are stored in reverse order, such that the 1's
#digit is at the head of the list. Write a function that adds the two numbers
#and returns the sum as a linked list stored in forward order.


from LN import LN, printList
        

def sumList(ln1, ln2):
    stack1 = list()
    stack2 = list()

    #populating stacks
    while ln1 != None:
        stack1.append(ln1.value)
        ln1 = ln1.nextNode
    while ln2 != None:
        stack2.append(ln2.value)
        ln2 = ln2.nextNode

    #padding stacks if one is smaller
    if len(stack1) != len(stack2):
        if len(stack1) > len(stack2):
            while len(stack2) < len(stack1):
                stack2.append(0)
        else:
            while len(stack1) < len(stack2):
                stack1.append(0)
                
    #creating answer linked list
    carry = 0
    answer = None
    while len(stack1) > 0:
        value = stack1.pop()+stack2.pop()+carry
        carry = value//10
        temp = LN(value%10,answer)
        answer = temp
    if carry != 0:
        temp = LN(carry,answer)
        answer = temp
    return answer


a = LN(6)
b = LN(1,a)
c = LN(7,b) #716

d = LN(2)
e = LN(9,d)
f = LN(5,e) #592

g = sumList(c,f)
printList(g) #1308



            
