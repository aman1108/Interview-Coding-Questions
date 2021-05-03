from collections import defaultdict
def solve(nums):
    n=len(nums)
    G=defaultdict(lambda :0)
    for i in range(len(nums)):
        G[nums[i]]=i
    ans=[]
    B=set()
    for i in range(n):
        for j in range(i+1,n):
            val=nums[i]+nums[j]
            if (G[-1*val]>j):
                v=[nums[i],nums[j],-1*val]
                v.sort()
                v1=(v[0],v[1],v[2])
                if v1 not in B:
                    
                    ans.append(list(v))
                    B.add(v1)
        
    return ans

print(solve([-1,0,1,2,-1,-4])) 
