#Maddy Chan 12/3/15
#InterviewBit
#Find out the maximum sub-array of non negative numbers from an array.
#The sub-array should be continuous. Maximum sub-array is defined in
#terms of the sum of the elements in the sub-array. Sub-array A is
#greater than sub-array B if sum(A) > sum(B).
#If there is a tie, then compare with segment's length and return
#which has maximum length. If there is still a tie, then return
#the segment with minimum starting index

def maxset(A):
    answers = []
    currentStart = 0
    #take all subarrays with positive numbers
    for i in range(len(A)):
        if A[i] < 0: 
            if i > currentStart:
                answers.append(A[currentStart:i])
            currentStart = i+1
        if i == len(A)-1 and i >= currentStart:
            answers.append(A[currentStart:i+1])
    #filter for the ones with the biggest sum
    maxSum = 0
    maxLists = []
    for a in answers:
        if sum(a) > maxSum:
            maxSum = sum(a)
            maxLists = [a]
        elif sum(a) == maxSum:
            maxLists.append(a)
    #filter for the ones with the largest length
    answer = []
    for a in maxLists:
        if len(a) > len(answer):
            answer = a
    return answer



print(maxset([76546,-1,-2,-3,34524564563465]))
