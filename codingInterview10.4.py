#Maddy Chan 12/7/15
#Cracking the Coding Interview 10.4
#Given a list which contains sorted, positive integers, no info about the size
#and where if you index somewhere out of bounds it will give -1,
#write an algorithm that will find x in the list.






def searchList(x: int, start: int, end: int, l: list):
    if start == end:
        return start if l[start] == x else -1
    elif l[end] > x or l[end] == -1:
        half = int((end-start)/2) + start
        if l[half] == x:
            return half
        elif l[half] > x or l[half] == -1:
            return searchList(x,start,half,l)
        else:
            return searchList(x,half,end-1,l)
    else:
        return searchList(x,end,end+(end-start),l)



l = [1,2,3,4,5,6,7,8,9,-1,-1,-1,-1,-1,-1,-1,-1]

print(searchList(9,0,6,l))
