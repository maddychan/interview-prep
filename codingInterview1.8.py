#Maddy Chan 12/6/15
#Cracking the Coding Interview 1.8
#Write an algorithm such that if an element in an MxN matrix is 0, its entire
#row and column are set to 0


def zeroMatrix(n: list):
    rows,column = set(),set()
    for i in range(len(n)):
        for j in range(len(n[a])):
            if n[i][j] == 0:
                rows.insert(i)
                columns.insert(j)
    for i in rows:
        for j in range(len(n[i])):
            n[i][j] = 0
    for i in range(len(n)):
        for j in columns:
            n[i][j] = 0




n = [[1,0,1],[2,2,2],[3,3,3]]
zeroMatrix(n)
print(n)
