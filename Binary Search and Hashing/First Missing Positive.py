def solve(nums):
    n=len(nums)
    for i in range(n):
        if (nums[i]>n or nums[i]<=0):
            nums[i]=n+1

    for i in range(n):
        v=abs(nums[i])
        if (0<v<=n):
            nums[v-1]=(-1*abs(nums[v-1]))
    
    for i in range(n):
        if (nums[i]>0):
            return i+1
    return n+1

print(solve([3,4,-1,1]))
    
