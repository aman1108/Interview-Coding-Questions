from collections import defaultdict
def solve(nums):
    G=defaultdict(lambda:0)
    for i in nums:
        G[i]+=1

    v=max(nums)
    x=G[v]*v
    y=max(x,G[v-1]*(v-1))
    for i in range(v-2,-1,-1):
        y,x=max(y,x+(G[i]*i)),y

    return y

print(solve([1,1,1]))
    
print(solve([2,2,3,3,3,4]))
