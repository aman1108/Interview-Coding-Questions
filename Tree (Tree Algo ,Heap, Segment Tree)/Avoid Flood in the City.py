from collections import defaultdict
import heapq
def solve(nums):
    n=len(nums)
    stk=[]

    ans=[-1]*n
    G=defaultdict(list)
    for i in range(n-1,-1,-1):
        G[nums[i]].append(i)

    for val in G:
        G[val].pop()
        
    rain=[]
    heapq.heapify(rain)
    flod=defaultdict(lambda:0)
    
    ans=[-1]*n
    for i in range(n):
        #print(i)
        if (nums[i]==0):
            if (len(rain)==0):
                ans[i]=1
            else:
                v=heapq.heappop(rain)
                if (v<i):
                    return []
                ans[i]=nums[v]
                flod[nums[v]]=0
        else:
            if(flod[nums[i]]==0):
                if(len(G[nums[i]])>0):
                    heapq.heappush(rain,G[nums[i]].pop())
                flod[nums[i]]=1
            else:
                return []
    return ans

print(solve([0,1,1]))
print(solve([1,2,3,4]))
print(solve([1,2,0,0,2,1]))
print(solve([1,2,0,2,1]))
