def solve(houses,heaters):
    houses.sort()
    heaters.sort()
    n=len(houses)
    m=len(heaters)

    heaters=[-1*float("inf")]+heaters+[float("inf")]

    ans=0
    j=0
    for i in range(n):
        while(houses[i]>heaters[j+1]):
            j=j+1
        ans=max(ans,min(houses[i]-heaters[j],heaters[j+1]-houses[i]))
    return ans


    
    '''houses.sort()
    heaters.sort()
    def fun(houses,heaters,x):
        n=len(houses)
        m=len(heaters)
        j=0
        for i in range(m):
            minv=heaters[i]-x
            maxv=heaters[i]+x
            while(j<n and houses[j]>=minv and houses[j]<=maxv):
                j=j+1
        
        if(j==n):
            return 1
        return 0

    low=0
    high=10**9
    ans=high
    while(low<=high):
        mid=(low+high)//2
        x=fun(houses,heaters,mid)
        if (x==1):
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    return ans'''

print(solve([10,15],[10,9]))
            
            
