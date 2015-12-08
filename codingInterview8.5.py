#Maddy Chan 12/7/15
#Cracking the Coding Interview 8.5
#Write a recursive function to multiply two positive integers without
#using the *operator. Minimize the number of operations you need to do using
#the +,-,or bit shifting operations

from collections import defaultdict



#tried to cache values at first and then realized I didn't need to do that

def multiply(n: int,m: int):
    print("called")
    if n == 0:
        return 0
    else:
        half = multiply(int(n/2),m)
        answer = half + half
        if n%2 != 0:
            answer+=m
        return answer


print(multiply(9,8))
