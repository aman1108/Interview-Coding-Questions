A=list(map(int,input().split()))
N=len(A)
cs=0
ms=A[0]

for i in range(N):
    cs=cs+A[i]
    ms=max(cs,ms)
    if (cs<0):
        cs=0

print(ms)
