#https://www.interviewbit.com/problems/maximum-path-in-triangle/
def solve(A):
    n=len(A)
    DP=[[0 for i in range(n+1)] for j in range(n)]

    for i in range(n):
        DP[-1][i]=A[-1][i]
    
    for i in range(n-2,-1,-1):
        for j in range(n):
            DP[i][j]=max(DP[i+1][j],DP[i+1][j+1])+A[i][j]

    #print(DP)
    return DP[0][0]

A = [
        [3, 0, 0, 0],
        [7, 4, 0, 0],
        [2, 4, 6, 0],
        [8, 5, 9, 3]
     ]

print(solve(A))
