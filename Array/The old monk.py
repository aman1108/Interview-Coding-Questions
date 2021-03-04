T=int(input())
for _ in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    j=0
    ans=0
    for i in range(n):
        while(j<=i and A[j]>B[i]):
            j=j+1
        ans=max(ans,i-j)
    print(ans)
