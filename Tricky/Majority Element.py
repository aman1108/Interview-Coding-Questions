def solve(nums):
    n=len(nums)
    ct=1
    lind=0
    ans=nums[0]
    for i in range(1,n):
        #print(i,ct,lind,ans)
        if(ct<=(i-lind)//2):
            ct=1
            ans=nums[i]
            lind=i
            
        elif (nums[i]==ans):
            ct=ct+1
    return ans

print(solve([3,2,3]))
            

print(solve([2,2,1,1,1,2,2]))
