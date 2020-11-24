A=list(map(int,input().split()))
N=len(A)
B=[0 for i in range(N)]
mv=A[N-1]

for i in range(N-2,0,-1):
    if (A[i]>mv):
        mv=A[i]
    B[i]=max(B[i+1],mv-A[i])

mnv=A[0]

for i in range(1,N):
    if (A[i]<mnv):
        mnv=A[i]
        
    B[i]=max(B[i-1],B[i]+(A[i]-mnv))

print(B[N-1])
