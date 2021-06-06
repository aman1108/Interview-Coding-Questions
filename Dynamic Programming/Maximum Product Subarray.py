def solve(nums):
    n=len(nums)
    ans=max(nums)

    mv=nums[0]
    vm=nums[0]
    for i in range(1,n):
        print(mv,vm,nums[i],mv*nums[i],vm*nums[i])
        mv,vm=max(nums[i],mv*nums[i],vm*nums[i]),min(nums[i],mv*nums[i],vm*nums[i])
        ans=max(ans,vm,mv)
        
    return ans

print(solve([-1,2,-3,-1]))
