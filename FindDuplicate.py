#Maddy Chan 12/1/15
#InterviewCake
#We have a list of integers, where:
#The integers are in the range 1..n1..n
#The list has a length of n+1n+1
#It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, and each duplicate may appear more than twice.
#Write a function which finds any integer that appears more than once in our list.
#we need to optimize for space!

#this function runs in O(NlogN) time, but only as much space as needed to
#store the return value plus one variable. It does mutate the input though.
#not mutating the input would either bring the space complexity to O(N)
#or bring the time complexity to O(N^2)

def findDuplicate(l: list):
    answer = []
    l.sort()
    index = 0
    while index < len(l)-1:
        if l[index] == l[index+1]:
            answer.append(l[index])
            while index < len(l) and l[index] == answer[-1]:
                index+=1
        else:
            index += 1
    return answer


print(findDuplicate([1,2,3,2,2,1,2,3,4,5,6,7,8,2,7]))
print(findDuplicate([]))
