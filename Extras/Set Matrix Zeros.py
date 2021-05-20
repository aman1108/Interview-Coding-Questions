def solve(matrix):
    n=len(matrix)
    m=len(matrix[0])
    f1,f2=1,1
    
    for i in range(n):
        for j in range(m):
            if (matrix[i][j]==0):
                if (i==0):
                    f2=0
                if(j==0):
                    f1=0
                
                matrix[i][0]=0
                matrix[0][j]=0

    for i in range(1,n):
        if (matrix[i][0]==0):
            for j in range(1,m):
                matrix[i][j]=0

    for j in range(1,m):
        if (matrix[0][j]==0):
            for i in range(1,n):
                matrix[i][j]=0

    print(f1,f2)
    if(f1==0):
        for i in range(n):
            matrix[i][0]=0
    if(f2==0):
        for j in range(m):
            matrix[0][j]=0

matrix=[[1,0,3]]
solve(matrix)
print(matrix)
