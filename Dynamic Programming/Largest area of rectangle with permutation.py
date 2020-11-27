def solve(A):
    n=len(A)
    m=len(A[0])

    DP=[[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if(A[i][j]==1):
                DP[i][j]=DP[i-1][j]+A[i][j]
    for i in range(n):
        DP[i].sort(reverse=True)

    ans=0
    print(DP)
    for i in range(n):
        rc=0
        for j in range(m):
            rc=rc+1
            ans=max(ans,rc*DP[i][j])
    print(ans)
        
A = [  [0,1,0,1,0],
        [0, 1,0,1,1],
        [1, 1,0,1,0]
    ]

solve(A)
