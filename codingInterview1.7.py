#Maddy Chan 12/2/15
#Cracking the Coding Interview 1.7
#Rotate a 2D matrix 90 degrees in place
 
from math import ceil


def rotate(n: list):
    N = len(n)
    last = N-1
    if N == 0:
        return n
    for i in range(ceil(N/2)):
        for j in range(i,last-i):
            n[i][j],n[j][last-i] = n[j][last-i],n[i][j]
            n[last-i][last-j],n[last-j][i] = n[last-j][i],n[last-i][last-j]
            n[i][j],n[last-i][last-j] = n[last-i][last-j],n[i][j]





n = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
rotate(n)
print(n[0])
print(n[1])
print(n[2])
print(n[3])
