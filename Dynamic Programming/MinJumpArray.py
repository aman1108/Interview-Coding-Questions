A=list(map(int,input().split()))
N=len(A)
B=[0 for i in range(N)]
sv=1
for i in range(N):
    if (sv==i):
        B[N-1]=-1
        break
    
    for j in range (sv,min(i+A[i]+1,N)):
        B[sv]=B[i]+1
        sv=sv+1

print(B[N-1])        
    
    
