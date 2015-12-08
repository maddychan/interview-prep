#Maddy Chan 12/7/15
#Cracking the Coding Interview 4.2
#Given a sorted array with unique integer elements, write an algorithm to
#create a binary search tree with minimal height


from TN import TN, printTree

def minimalTree(TL: list):
    if len(TL) == 0:
        return None
    elif len(TL) == 1:
        return TN(TL[0])
    else:
        half = int(len(TL)/2)
        return TN(TL[half],minimalTree(TL[:half]),minimalTree(TL[half+1:]))

##l = [1,2,3,4,5,6,7,8,9]
##
##print(printTree(minimalTree(l),""))
