def solve(List,k):
    n=len(List)
    lmx=[0 for i in range(n)]
    rmx=[n-1 for i in range(n)]

    stk=[]
    for i in range(n):
        while(len(stk)>0 and List[stk[-1]]>=List[i]):
            stk.pop()
        if (len(stk)>0):
            lmx[i]=stk[-1]+1
        stk.append(i)

    stk=[]
    for i in range(n-1,-1,-1):
        while(len(stk)>0 and List[stk[-1]]>=List[i]):
            stk.pop()
        if (len(stk)>0):
            rmx[i]=stk[-1]-1
        stk.append(i)

    ans=0
    #print(lmx,rmx)
    for i in range(n):
        x,y=lmx[i],rmx[i]
        if (k>=x and k<=y):
            ans=max(ans,List[i]*(y-x+1))

    return ans

print(solve([1,4,3,7,4,5],3))
print(solve([5,5,4,5,4,1,1,1],0))
