N,S=map(int,input().split())

DP=[[0 for i in range(S+1)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(1,min(S+1,9*N+1):
        ans=0
        for k in range(10):
            if (i==1 and j==0):
                DP[i][j]=0

            elif (S-j>=0):
                DP[i][j]=DP[i-1][j-1]+1

ans=0
