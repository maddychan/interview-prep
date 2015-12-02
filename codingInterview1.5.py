#Maddy Chan 11/28/15
#Cracking the Coding Interview 1.5
#Given two strings, write a function to check of they are one (or zero) edits away

#this is not as optimal as the back of the book, but it's as close as I got. still learning! 

from collections import defaultdict

def oneAway(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        for i in range(len(s1)):            
            if s1[i] != s2[i]:
                #if the strings aren't equal when you replace the different character, then return false
                if s1 != s2[0:i]+s1[i] + ("" if len(s2) == i+1 else s2[i+1:]):
                    return False
                return True
        return True
    
    elif abs(len(s1)-len(s2)) == 1:
        longer, shorter = (s1,s2) if len(s1) > len(s2) else (s2,s1)
        for i in range(len(shorter)):
            if shorter[i] != longer[i]:
                #if the strings aren't equal when you take out the different character, then return false
                if shorter != ("" if i == 0 else longer[0:i])+longer[i+1:]:
                    return False
                return True
        return True
    
    else:
        return False
    




print(oneAway("pale", "ple"))
print(oneAway("pale", "pales"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake")) #false
print(oneAway("pale", "ale"))
print(oneAway("ale", "pales")) #false
print(oneAway("fele", "bale")) #false
print(oneAway("pale", "please")) #false
print(oneAway("pale", ""))      #false
print(oneAway("", "")) 
