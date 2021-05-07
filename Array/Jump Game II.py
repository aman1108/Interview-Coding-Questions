def solve(nums):
    n=len(nums)
    cur=0
    nmax=nums[0]
    cnt=0
    DP=[0 for i in range(n)]
    i=0
    while(i<n):
        j=i
        while (j<n and j<=cur):
            nmax=max(nmax,j+nums[j])
            DP[j]=cnt
            j=j+1
        cnt=cnt+1
        cur=nmax
        i=j           

    return DP[-1]

    '''
    O(n^2)
    n=len(nums)
    ans=0
    DP=[10**9 for i in range(n)]
    DP[-1]=0
    for i in range(n-2,-1,-1):
        for j in range(i+1,min(i+nums[i]+1,n)):
            DP[i]=min(DP[i],1+DP[j])

    return DP[0]'''

print(solve([1,2,1,1,1]))
