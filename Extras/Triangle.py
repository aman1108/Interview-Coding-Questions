def solve(triangle):
    n=len(triangle)
    DP=[float("inf") for i in range(n)]
    DP[0]=triangle[0][0]

    for i in range(1,n):
        DP1=DP.copy()
        for j in range(i+1):
            if (j==0):
                DP[j]=DP1[j]+triangle[i][j]
            elif(j==i):
                DP[j]=DP1[j-1]+triangle[i][j]
            else:
                DP[j]=min(DP1[j],DP1[j-1])+triangle[i][j]
        print(DP)
    return min(DP)

print(solve([[2],[3,4],[6,5,7],[4,1,8,3]]))
                
