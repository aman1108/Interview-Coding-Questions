def solve(n):
    if (n==1):
        return 10
    mod=(10**9)+7
    G={}
    G[0]=[4,6]
    G[1]=[6,8]
    G[2]=[9,7]
    G[3]=[4,8]
    G[4]=[3,9,0]
    G[5]=[]
    G[6]=[7,1,0]
    G[7]=[2,6]
    G[8]=[1,3]
    G[9]=[4,2]

    DP=[1 for i in range(10)]
    DP[5]=0
    for k in range(n-1):
        DP1=[0]*10
        for i in range(10):
            for j in G[i]:
                DP1[j]=(DP1[j]+DP[i])%mod
                
        DP=DP1.copy()
        #print(DP)
        
    ans=0
    for i in range(10):
        ans=(ans+DP[i])%mod
    return ans

print(solve(3131))
