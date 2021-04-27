from collections import deque
def solve(nums,k):
    n=len(nums)
    Q=deque([])

    ans=[]

    for i in range(k):
        while (len(Q)>0 and nums[Q[-1]]<nums[i]):
            Q.pop()
        Q.append(i)

    #print(Q)
    ans.append(nums[Q[0]])

    for i in range(k,n):
        if (Q[0]<=(i-k)):
            Q.popleft()

        while (len(Q)>0 and nums[Q[-1]]<nums[i]):
            Q.pop()
        Q.append(i)
        #print(Q)
        ans.append(nums[Q[0]])
        
    return ans
    

print(solve([1,3,2],3))
print(solve([1,3,-1,-3,5,3,6,7],3))
print(solve([1],1))
print(solve([9,11],2))
print(solve([7,7,6,5,4,3,2,1],3))
