#Maddy Chan 11/30/15
#Cracking the Coding Interview 6.7
#In the new post-apocalyptic world, the world queen is desperately concerned
#about the birth rate. Therefore, she decrees that all families should ensure
#that they have one girl or else they face massive fines. If all families abide
#by this policy - that is, they have continue to have children until they have
#one girl, at which point they immediately stop - what will the gener ratio of
#the new generation be? (Assume that the odds of someone having a boy or girl on
#any given pregnancy is equal.


#Each time the population has babies, half the babies will be girls and half
#will be boys. When the families that had boys reproduce again, that subset
#will also get half girls and half boys. This keeps going iteratively down
#until each family has one girl, and the ratio will be close to 1:1


#popRatio takes the number of families in a population and gives the
#ratio of girls to guys in the next generation. I realize that this is different
#than what was at the back of the book but I think it's simpler.
import random

def popRatio(n: int):
    girls = 0
    boys = 0
    #each iteration of the while loop simulates another round of births
    while n > 1:
        for i in range(n):
            g = random.randint(0,1)
            n2 = 0
            if g == 1:
                girls+= 1
            else:
                boys+= 1
                n2 += 1
        n = n2
    return girls/boys

print(popRatio(100))
print(popRatio(1000))
print(popRatio(10000))
print(popRatio(100000)) #converges closer to 1

