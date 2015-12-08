#Maddy Chan Tree Node module

class TN:
    def __init__(self,value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def printTree(TN,indent):
    if TN == None:
        return ""
    return printTree(TN.left,indent+"  ")+"\n"+indent+str(TN.value)+printTree(TN.right,indent+"  ")



##q = TN(1)
##w = TN(2)
##e = TN(3)
##r = TN(4)
##t = TN(5,q,w)
##y = TN(6,e,r)
##a = TN(7,t,y)
##
##print(printTree(a,""))
