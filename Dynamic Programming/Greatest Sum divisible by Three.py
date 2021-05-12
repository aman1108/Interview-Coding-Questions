def solve(nums):
    n=len(nums)
    DP=[0,0,0]
    for i in range(n):
        v=nums[i]
        for x in (DP.copy()):
            DP[(v+x)%3]=max(DP[(v+x)%3],v+x)
        print(DP)
    return DP[0]

print(solve([1,2,3,4,4]))
    
