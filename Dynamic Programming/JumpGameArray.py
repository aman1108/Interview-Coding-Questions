A=list(map(int,input().split()))
N=len(A)

DP=[0 for i in range(N)]
DP[N-1]=1
for i in range(N-2,-1,-1):
    v=A[i]
    for j in range(i+1,min(i+v+1,N)):
        DP[i]=max(DP[j],DP[i])

print(DP)
