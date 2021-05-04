def solve(coins,amount):
    n=len(coins)
    DP=[10**9 for i in range(amount+1)]
    DP[0]=0
    for i in range(n):
        for j in range(amount+1-coins[i]):
            DP[j+coins[i]]=min(DP[j+coins[i]],1+DP[j])
            
    if(DP[amount]==10**9):
        return -1
    return DP[amount]

print(solve([1,2,5],11))

