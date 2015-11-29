#Maddy Chan 11/28/15
#sorts, sorts, sorts!
#sorts take a list and a greater than function
#the greater than function is there so that the sort will work for any data type

from collections import defaultdict

def gtInt(a:int,b:int):
    return a > b

#selection sort

def selection(l: list, gt):
    for i in range(len(l)):
        minIndex = i
        for j in range(i+1, len(l)):
            if gt(l[minIndex],l[j]):
                minIndex = j
        temp = l[minIndex]
        l[minIndex] = l[i]
        l[i] = temp

#insertion sort

def insertion(l:list, gt):
    for i in range(1,len(l)):
        comp_index = i-1
        current = i
        while comp_index >=0 and gt(l[comp_index],l[current]):
            temp = l[current]
            l[current] = l[comp_index]
            l[comp_index] = temp
            comp_index -=1
            current-=1


#merge sort

def merge(l: list, gt):
    if len(l) == 1:
        return l
    half = int(len(l)/2)
    front = merge(l[:half],gt)
    back = merge(l[half:],gt)
    answer = []
    while len(front) != 0 and len(back) != 0:
        if gt(front[0],back[0]):
            answer.append(back[0])
            back.pop(0)
        else:
            answer.append(front[0])
            front.pop(0)
    if len(front) == 1:
        answer.append(front[0])
    else:
        answer.append(back[0])
    return answer

#bucket sort

def bucket(l:list):
    answer_dict = defaultdict(int)
    for a in l:
        answer_dict[a] +=1
    answer = []
    for a in sorted(answer_dict.keys()):
        for i in range(answer_dict[a]):
            answer.append(a)
    return answer

l = [3,2,5,4,2,3,5,4,3,1]
#print(merge(l,gtInt))
print(bucket(l))
