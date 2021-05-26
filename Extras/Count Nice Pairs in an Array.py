from collections import defaultdict
def solve(nums):
    n=len(nums)
    G=defaultdict(lambda:0)
    for i in range(n):
        v=int(str(nums[i])[::-1])
        G[v-nums[i]]+=1
    ans=0
    mod=(10**9)+7

    for val in G:
        cnt=G[val]
        ans=(ans+((cnt)*(cnt-1))//2)%mod

    return ans

print(solve([42,11,1,97]))
        
