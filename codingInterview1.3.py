#Maddy Chan 11/28/15
#Cracking the Coding Interview #1.3
#Write a method to replace all spaces in a string with '%20'
#You may assume that the string has sufficient space at the end to
#hold the additional characters, and that you are given the 'true'
#length of the string

#The book describes a solution that uses a mutable string, but since
#strings in python are immutable, this solution is more efficient

def replace(s:str):
    listOfWords = s.strip().split(" ")
    answer = ""
    for word in listOfWords:
        answer = answer+word+"%20"
    return answer
        


print(replace("hello there I like pants         "),20)
