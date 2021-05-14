from collections import defaultdict
def solve(nums):
    m=len(nums)
    stk=[]
    ans=[-1 for i in range(m)]
    for i in range(m-1,-1,-1):
        while(len(stk)>0 and stk[-1]<=nums[i]):
            stk.pop()
        if (len(stk)>0):
            ans[i]=stk[-1]
        stk.append(nums[i])

    
    for i in range(m-1,-1,-1):
        while(len(stk)>0 and stk[-1]<=nums[i]):
            stk.pop()
        if (len(stk)>0):
            ans[i]=stk[-1]
        stk.append(nums[i])

    return ans
print(solve([3,8,4,1,2]))
