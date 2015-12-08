#Maddy Chan 12/7/15
#Cracking the Coding Interview 8.11
#Calculate the number of ways to represent n cents with quarters, nickels and dimes


#almost got it... need to remember that caching values is a thing >___<
def coinCombos(n: int, coins: list):
    if n == 0:
        return 1
    elif n < 0 or len(coins) == 0:
        return 0
    else:
        if len(coins) == 1:
            return 1 if (n/coins[0])%1 == 0 else 0
        answer = 0
        for a in coins:
            temp,tempList = n,list(coins)
            tempList.remove(a)
            while temp > 0:
                temp-=a
                answer += coinCombos(temp,tempList)
        return answer



print(coinCombos(50,[25,10,5]))
