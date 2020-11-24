A=input()
B=input()
C=input()

n,m,l=len(A),len(B),len(C)
DP=[[[0 for i in range(l+1)] for j in range(m+1)] for k in range(n+1)]

DP[0][0][0]=1
for i in range(n+1):
    for j in range(m+1):
        for k in range(l+1):
            if (k==0 and (i!=0 or j!=0)):
                DP[i][j][k]=0

            elif (k==0 and i==0 and j==0):
                DP[i][j][k]=1

            elif (i==0 and j==0):
                DP[i][j][k]=0
                
            elif(i==0):
                if (B[j-1]==C[k-1]):
                    DP[i][j][k]=DP[i][j-1][k-1]

            elif(j==0):
                if (A[i-1]==C[k-1]):
                    DP[i][j][k]=DP[i-1][j][k-1]

            else:
                if (B[j-1]==C[k-1] and A[i-1]==C[k-1]):
                    DP[i][j][k]=max(DP[i-1][j][k-1],DP[i][j-1][k-1])

                elif(B[j-1]==C[k-1]):
                    DP[i][j][k]=DP[i][j-1][k-1]

                elif(A[i-1]==C[k-1]):
                    DP[i][j][k]=DP[i-1][j][k-1]
                    

print(DP[n][m][l])
                
