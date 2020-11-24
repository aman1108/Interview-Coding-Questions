A=list(map(int,input().split()))
N=len(A)

ans=0
c=0
for i in range(N-1,-1,-1):
    if (A[i]<=c):
        ans=ans+c-A[i]
    c=A[i]

print(ans)
    
    
