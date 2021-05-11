def solve(nums,target):
    n=len(nums)
    hmap=set([0])
    s=0
    ans=0
    for i in range(n):
        s=s+nums[i]
        if (s-target in hmap):
            ans=ans+1
            hmap=set()
            s=nums[i]
        hmap.add(s)
        
    return ans

print(solve([-5,5,-4,5,4],5))
print(solve([0,0,0],0))
