def solve(nums):
    nums.sort()
    n=len(nums)
    DP=[[1,i] for i in range(n)]

    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if (nums[j]%nums[i]==0):
                if (1+DP[j][0]>DP[i][0]):
                    DP[i][0]=1+DP[j][0]
                    DP[i][1]=j
    v=max(DP)
    ind=DP.index(v)
    ans=[]
    for i in range(v[0]):
        ans.append(nums[ind])
        ind=DP[ind][1]
    return ans

print(solve([1]))
