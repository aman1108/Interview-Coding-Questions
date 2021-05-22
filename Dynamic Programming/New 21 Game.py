from collections import deque
def solve(n,k,maxPts):
    ans=0
    tot=0
    ctr=maxPts
    stk=[0]*(maxPts)
    stk=deque(stk)
    for i in range(min(n,k+maxPts-1),-1,-1):
        if (i>=k):
            x=stk.popleft()
            tot=tot+1
            stk.append(1)
            
        else:
            x=stk.popleft()
            ans=(tot/maxPts)
            stk.append(ans)
            tot=tot-x+ans
        print(i,tot,ans)
        
    return ans

print(solve(185,183,2))
#print(solve(21,17,10)) 
#print(solve(5,4,3))
        
    
