def solve(gas,cost):
    n=len(gas)
    
    tot=0
    if (sum(gas)-sum(cost)<0):
        return -1
    
    ans=0
    for i in range(n):
        tot=tot+gas[i]-cost[i]
        if (tot<0):
            tot=0
            ans=(i+1)%n
    return ans
    

    '''n=len(gas)
    nums=[gas[i]-cost[i] for i in range(n)]
    #print(nums)
    tot=sum(nums)
    if (tot<0):
        return -1

    pref=[0]*n
    suff=[0]*n
    s=0
    for i in range(1,n):
        pref[i]=min(pref[i-1],s+nums[i-1])
        s=s+nums[i-1]

    s=0
    for i in range(n-2,-1,-1):
        suff[i]=min(suff[i-1],s+nums[i+1])
        s=min(s+nums[i+1],0)
    
    s=nums[-1]
    if (nums[-1]>=0 and nums[-1]+pref[-1]>=0 and nums[-1]+suff[-1]>=0):
        return n-1
    
    for i in range(n-2,-1,-1):
        s=s+nums[i]
        if (nums[i]>=0 and s>=0 and nums[i]+suff[i]>=0 and s+pref[i]>=0):
            return i
    return -1'''
        
        
print(solve([5,1,2,3,4],[4,4,1,5,1]))
        
    
        
