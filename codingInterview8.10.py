#Maddy Chan 12/7/15
#Cracking the Coding Interview 8.10
#Given a point on a 2d array, fill the surrounding section with a specified color






def fill(position: tuple,color, array: list):
    if len(array) == 0:
        return 
    toFill = array[position[0]][position[1]]
    array[position[0]][position[1]] = color
    directions = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(1,-1),(-1,1)]
    height = len(array)
    width = len(array[0])
    for i,j in directions:
        a,b = position[0]+i,position[1]+j
        if a >=0 and b >= 0 and a < height and b < width and array[a][b] == toFill:
            fill((a,b),color,array)



l = [[1,2,2,2,1],[3,1,2,1,3],[3,3,1,3,3],[3,1,2,1,3],[1,2,2,2,1]]

fill((2,2),6,l)

for a in l:
    print(a)
