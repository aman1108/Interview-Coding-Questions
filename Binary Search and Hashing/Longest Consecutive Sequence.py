def solve(nums):
        n=len(nums)
        G={}
        for i in nums:
            G[i]=1
        ans=0
        for val in G:
            if val-1 not in G:
                temp=val
                tans=1
                while temp+1 in G:
                    temp=temp+1
                    tans=tans+1

                ans=max(ans,tans)
        return ans


