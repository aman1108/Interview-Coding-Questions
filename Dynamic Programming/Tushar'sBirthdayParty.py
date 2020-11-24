A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

n=max(A)
m=len(B)


MA=[0 for i in range(n+1)]
for i in range(1,n+1):
    ans=float("Inf")
    for j in range(m):
        if (i-B[j]>=0):
            ans=min(ans,MA[i-B[j]]+C[j])

    MA[i]=ans


fa=0
for i in range(len(A)):
    fa=fa+MA[A[i]]

print(fa)
    
        
        
        
