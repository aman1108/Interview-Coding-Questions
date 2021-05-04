from collections import defaultdict
def solve(nums,target):
    G={}
    for i in range(len(nums)):
        if target-nums[i] in G:
            return [G[target-nums[i]],i]
        G[nums[i]]=i

print(solve([3,2,4],6))
        
