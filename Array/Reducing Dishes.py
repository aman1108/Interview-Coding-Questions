def solve(satisfaction):
    A=satisfaction
    n=len(A)
    A.sort()
    suff=[A[i] for i in range(n)]
    temp=n*A[-1]
    for i in range(n-2,-1,-1):
        suff[i]=suff[i]+suff[i+1]
        temp=temp+((i+1)*A[i])
    ans=temp

    for i in range(n):
        temp=temp-suff[i]
        ans=max(ans,temp)

    return ans
        
    
    
    '''
    O(nlogn + n^2)
    A.sort()
    ans=0
    for i in range(n):
        temp=0
        for j in range(i,n):
            temp=temp+A[j]*(j-i+1)
        ans=max(ans,temp)
    return ans'''

print(solve([-1,-8,0,5,-9]))
print(solve([-2,5,-1,0,3,-3]))
print(solve([4,3,2]))
print(solve([-4,-3,-2]))
