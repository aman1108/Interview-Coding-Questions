def solve(nums):
    n=len(nums)
    DP=[0 for i in range(32)]
    for val in nums:
        for j in range(32):
            if (val&(1<<j)):
                DP[j]=DP[j]+1

    ans=0
    for i in range(32):
        ans=ans+(DP[i]*(n-DP[i]))
    return ans

print(solve([4]))
