def solve(nums):
    n=len(nums)
    s=sum(nums)
    if (s%2==1):
        return 0
    target=s//2
    DP=[0 for i in range(target+1)]

    DP[0]=1
    for i in range(n):
        for j in range(target,-1,-1):
            if (j+nums[i]<=target and DP[j]==1):
                DP[j+nums[i]]=1

    return DP[-1]

print(solve([2,3,5]))
            
            
    
