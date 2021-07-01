def solve(prices):
    n=len(prices)
    DP=[-1*float("inf"),0,0,-1*float("inf")]
    for val in prices:
        DP1=DP.copy()

        DP[0]=max(DP[0],DP1[2]-val)
        DP[1]=max(DP1[1],DP1[0]+val,DP1[-1]+val)
        DP[2]=max(DP[2],DP1[1])
        DP[3]=max(DP1[3],DP1[0])
        print(DP)
    return max(DP)

print(solve([1,2,3,4,5,6,7,8,9,8,6]))
        
            
            
