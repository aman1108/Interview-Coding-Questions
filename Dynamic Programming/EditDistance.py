A=input()
B=input()

n,m=len(A),len(B)

DP=[[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n+1):
    for j in range(m+1):

        if (i==0):
            DP[i][j]=j
            
        elif(j==0):
            DP[i][j]=i
            
        elif (A[i-1]!=B[j-1]):
            DP[i][j]=1+min(DP[i-1][j-1],DP[i-1][j],DP[i][j-1])

        else:
            DP[i][j]=DP[i-1][j-1]

print(DP)
print(DP[n][m])
        
