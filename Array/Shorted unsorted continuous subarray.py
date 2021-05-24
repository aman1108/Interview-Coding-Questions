def solve(nums):
    n=len(nums)
    mv=float("inf")
    flag=0
    for i in range(1,n):
        if(flag==1):
            mv=min(mv,nums[i])
        elif (nums[i]<nums[i-1]):
            flag=1
            mv=nums[i]
    if(flag==0):
        return 0
    low=-1
    for i in range(n):
        if (mv<nums[i]):
            low=i
            break
        
    
    mv=-1*float("inf")
    flag=0
    for i in range(n-2,-1,-1):
        if(flag==1):
            mv=max(mv,nums[i])
        elif (nums[i]>nums[i+1]):
            flag=1
            mv=nums[i]

    for i in range(n-1,-1,-1):
        if (mv>nums[i]):
            high=i
            break
    return high-low+1


    ''' Stack Soln
    n=len(nums)
    stk=[]
    low=-1
    flag=0
    for i in range(n):
        while (len(stk)>0 and nums[i]<nums[stk[-1]]):
            flag=1
            stk.pop()
        if(flag==0):
            stk.append(i)

    if(len(stk)==n):
        return 0
    
    if(len(stk)>0):
        low=max(low,stk[-1])

        
    stk=[]
    high=n
    flag=0
    for i in range(n-1,-1,-1):
        while (len(stk)>0 and nums[i]>nums[stk[-1]]):
            flag=1
            stk.pop()
        if(flag==0):
            stk.append(i)

    if(len(stk)>0):
        high=min(high,stk[-1])
    
    #print(high,low)
    return high-low-1'''


print(solve([2,6,8,10,4,3,15,17]))
