import bisect
def solve(nums):    
    n=len(nums)
    DP=[10**5]*(n)
    ans=0
    for i in range(n):
        v=bisect.bisect_left(DP,nums[i])
        DP[v]=nums[i]
        ans=max(ans,v+1)
        
    return ans

    '''O(n^2)
    n=len(nums)
    DP=[1 for i in range(n)]
    for i in range(n):
        for j in range(0,i):
            if (nums[i]>nums[j]):
                DP[i]=max(DP[i],1+DP[j])
        
    return max(DP)'''

#print(solve([10,9,2,5,3,7,101,19]))
print(solve([0,1,0,3,2,3]))
