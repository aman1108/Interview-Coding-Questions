A=list(map(int,input().split()))
N=len(A)
A.sort()

B=[]
i=0
while(i<N):
    if(i==N-1):
        B.append(A[i])
    else:
        B.append(A[i+1])
        B.append(A[i])
    i=i+2

print(*B)
