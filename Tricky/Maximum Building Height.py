from collections import deque
def solve(n,restrictions):
    m=len(restrictions)
    A=restrictions
    A=[[1,0]]+A+[[n,n-1]]
    A.sort()
    ans=[0 for i in range(m+2)]
    v1,v2=1,0
    for i in range(m+2):
        gap=A[i][0]-v1
        ans[i]=min(v2+gap,A[i][1])
        v1,v2=A[i][0],ans[i]

    
    v1,v2=n,10**18
    for i in range(m,-1,-1):
        gap=v1-A[i][0]
        ans[i]=min(ans[i],v2+gap,A[i][1])
        v1,v2=A[i][0],ans[i]

    cnt=0
    for i in range(1,m+2):
        x1,y1=A[i-1][0],ans[i-1]
        x2,y2=A[i][0],ans[i]
        cnt=max(cnt,max(y1,y2)+((x2-x1-abs(y1-y2))//2))
        
    return cnt

print(solve(10,[[8,5],[9,0],[6,2],[4,0],[3,2],[10,0],[5,3],[7,3],[2,4]]))
print(solve(6,[]))
print(solve(5,[[2,1],[4,1]]))
print(solve(10,[[5,3],[2,5],[7,4],[10,3]]))
        
        
        
