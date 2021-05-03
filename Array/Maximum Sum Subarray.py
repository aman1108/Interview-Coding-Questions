def solve(nums):
    n=len(nums)
    s=0
    ans=nums[0]
    for i in range(n):
        s=s+nums[i]
        ans=max(ans,s)
        if (s<0):
            s=0
    return ans
