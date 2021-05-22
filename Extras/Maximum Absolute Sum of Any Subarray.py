def solve(nums):
    n=len(nums)
    ans=0
    temp=0

    for i in range(n):
        if (temp<0):
            temp=0
        temp=temp+nums[i]
        ans=max(ans,abs(temp))

    temp=0
    for i in range(n):
        if (temp>0):
            temp=0
        temp=temp+nums[i]
        ans=max(ans,abs(temp))

    return ans

print(solve([-2,-5,1,-4,3,-2]))
