def solve(nums):
    n=len(nums)
    A=[0 for i in range(n+2)]
    for i in range(n-1,-1,-1):
        A[i]=max(nums[i]+A[i+2],A[i+1])
    return A[0]

print(solve([1,2,3,1]))
