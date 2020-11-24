A=list(map(int,input().split()))
N=len(A)

maxv=[0 for i in range(N)]    
minv=[0 for i in range(N)]

maxv[0]=minv[0]=A[0]

ans=A[0]

for i in range(1,N):
    if (A[i]>0):
        maxv[i]=max(A[i],maxv[i-1]*A[i])
        minv[i]=min(A[i],minv[i-1]*A[i])
    else:
        maxv[i]=max(A[i],minv[i-1]*A[i])
        minv[i]=min(A[i],maxv[i-1]*A[i])

    ans=max(ans,maxv[i])
    print(maxv,minv)

print(ans)
