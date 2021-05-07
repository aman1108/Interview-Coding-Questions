def solve(nums,k):
    n=len(nums)
    nums.sort()
    ans=1
    cnt=1
    j=0
    val=0
    for i in range(1,n):
        val=val+cnt*(nums[i]-nums[i-1])
        cnt=cnt+1
        while (val>k):
            val=val-(nums[i]-nums[j])
            j=j+1
            cnt=cnt-1
        ans=max(ans,cnt)
    return ans
        
        


print(solve([3,9,6],2))
print(solve([1,4,8,13],5))
print(solve([1,1,4],3))
