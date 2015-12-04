#Maddy Chan 11/28/15
#sorts, sorts, sorts!
#sorts take a list and a greater than function
#the greater than function is there so that the sort will work for any data type

from collections import defaultdict

def gtInt(a:int,b:int) -> bool:
    return a > b

#selection sort - mutates list

def selection(l: list, gt) -> None:
    for i in range(len(l)):
        minIndex = i
        for j in range(i+1, len(l)):
            if gt(l[minIndex],l[j]):
                minIndex = j
        l[minIndex], l[i] = l[i], l[minIndex]

#insertion sort - mutates list

def insertion(l:list, gt) -> None:
    for i in range(1,len(l)):
        comp_index, current = i-1, i
        while comp_index >=0 and gt(l[comp_index],l[current]):
            l[current], l[comp_index] = l[comp_index], l[current]
            comp_index -=1
            current -=1


#merge sort - returns sorted list

def merge(l: list, gt) -> list:
    #if base case of one element, return that element
    if len(l) == 1:
        return l
    
    #setting variables - halfpoint, answer list, the sorted front and back arrays
    half, answer = int(len(l)/2), []
    front, back = merge(l[:half],gt), merge(l[half:],gt)

    #merging the two sorted lists into one
    while len(front) != 0 and len(back) != 0:
        if gt(front[0],back[0]):
            answer.append(back[0])
            back.pop(0)
        else:
            answer.append(front[0])
            front.pop(0)

    #adding the last leftover element
    answer.append(front[0] if len(front) == 1 else back[0])
    return answer

#bucket sort - returns sorted list

def bucket(l:list) -> list:
    answer_dict, answer = defaultdict(int), []
    for a in l:
        answer_dict[a] +=1
    for a in sorted(answer_dict.keys()):
        for i in range(answer_dict[a]):
            answer.append(a)
    return answer

#quick sort - returns sorted list - NOT DONE YET

##def quick(l:list, gt):
##    if len(l) == 1 or len(l) == 0:
##        return l
##    pivot = l[-1]
##    start = 0
##    end = len(l)-1
##    while(start != end):
##        while gt(pivot,l[start]) and start < end:
##            start+=1
##        while gt(l[end],pivot) and end > start:
##            end-=1
##        l[start],l[end] = l[end],l[start]
##    answer = quick(l[0:start],gt)
##    answer.append(l[start])
##    answer.extend(quick(l[end+1:],gt))
##    return answer
                   

#l = [3,2,5,4,2,3,5,4,3,1]
l = [3,2,4,5,1,6,9,7,8]
#l = ['a','b','c','y','t','e','j']
#print(merge(l,gtInt))
#print(quick(l,gtInt))
#insertion(l,gtInt)
#print(l)
