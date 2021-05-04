def solve(nums):
    n=len(nums)
    DP=[0 for i in range(n+1)]
    DP1=[0 for i in range(n+1)]
    ans=max(nums)
    for i in range(n-2,-1,-1):
        DP[i]=max(nums[i]+DP[i+2],DP[i+1])
        DP1[i]=max(nums[i+1]+DP1[i+2],DP1[i+1])
        ans=max(ans,DP[i],DP1[i])

    return ans

print(solve([1,3,1,3,100]))
    
    
