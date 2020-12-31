#https://www.interviewbit.com/problems/maximum-path-in-triangle/
def solve(A):
    n=len(A)
    DP=[[0 for i in range(n+1)] for j in range(n)]

    for i in range(n):
        DP[-1][i]=A[-1][i]
    
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            DP[i][j]=min(DP[i+1][j],DP[i+1][j+1])+A[i][j]

    #print(DP)
    return DP[0][0]

A = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
     ]

print(solve(A))
