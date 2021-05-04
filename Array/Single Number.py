def solve(nums):
    ans=0
    for i in range(len(nums)):
        ans=ans^nums[i]
    return ans
    
