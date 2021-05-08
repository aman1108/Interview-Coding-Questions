def solve(nums):
    nums.append(10**9)
    n=len(nums)
    i=1
    cnt=1
    ans=0
    val=0
    while(i<n):
        if (val==(nums[i]-nums[i-1])):
            cnt=cnt+1
        else:
            val=(nums[i]-nums[i-1])
            v=cnt-2
            ans=ans+max((v*(v+1))//2,0)
            cnt=2
        i=i+1
    return ans

print(solve([1,4,8,11]))
