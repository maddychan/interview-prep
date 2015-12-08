#Maddy Chan 12/7/15
#Cracking the Coding Interview 8.8
#Write a method to compute all permutations of a string of characters that are
#not necessarily unique

from collections import defaultdict




def permutation(string: str):
    if len(string) == 1:
        return [string]
    store = defaultdict(int)
    answer = []
    for a in string:
        if store[a] == 0:
            temp = permutation(string.replace(a,"",1))
            for i in range(len(temp)):
                temp[i]+=a
            answer.extend(temp)
            store[a]+=1
    return answer


print(sorted(permutation("abcabc")))
                               
            
