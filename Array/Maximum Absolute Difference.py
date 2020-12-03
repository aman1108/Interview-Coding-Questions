def solve(A):
    n=len(A)
    mt1=[]
    mt2=[]

    for i in range(n):
        mt1.append(A[i]-i)
        mt2.append(A[i]+i)
    
    ans=-(10**18)
    mv=10**18

    
    for i in range(n-1,-1,-1):
        mv=min(mt1[i],mv)
        ans=max(ans,mt1[i]-mv)

    
    
    mv=10**18
    for i in range(n):
        mv=min(mt2[i],mv)
        #print(mv)
        ans=max(ans,mt2[i]-mv)

    #print(mt2,ans)
    return ans

print(solve([ -98, -5, 37, -97, 38, 22, 70, 42, 61, 84 ]))
        
    
