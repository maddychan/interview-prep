#Maddy Chan 12/3/15
#InterviewBit
#You are in an infinite 2D grid where you can move in any of the 8 directions
#You are given a sequence of points and the order in which you need to cover
#the points. Give the minimum number of steps in which you can achieve it.
#You start from the first point.

#input format: X is the list of X coordinates, Y is the list of Y coordinates

def coverPoints(X, Y):
    steps = 0
    for i in range(len(X)-1):
        x,y = abs(X[i] - X[i+1]), abs(Y[i] - Y[i+1])
        l = [x,y]
        l.sort()
        steps += l[0]+(l[1] - l[0])
    return steps


print(coverPoints([1,5,2],[1,4,7])) #should return 7 steps
