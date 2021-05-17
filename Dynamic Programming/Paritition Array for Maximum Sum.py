def solve(arr,k):
    n=len(arr)
    DP=[0]*(n+1)

    for i in range(n-1,-1,-1):
        v=0
        for j in range(i,min(i+k,n)):
            v=max(arr[j],v)
            DP[i]=max(DP[i],v*(j-i+1)+DP[j+1])
    return DP[0]

print(solve([1,15,7,9,2,5,10],3))
    
print(solve([1,4,1,5,7,3,6,1,9,9,3],4))

print(solve([0,1],2))
