import copy
def solve(A,B):
    k=A
    A=B
    n=len(A)
    m=len(A[0])

    #temp=copy.deepcopy(A)
    temp=[]
    for i in range(n):
            temp.append([])
            for j in range(m):
                temp[i].append(A[i][j])
    for _ in range(k):
        for i in range(n):
            for j in range(m):

                if (i>0):
                    A[i][j]=max(temp[i-1][j],A[i][j])
                if (j>0):
                    A[i][j]=max(temp[i][j-1],A[i][j])
                if (i<(n-1)):
                    A[i][j]=max(temp[i+1][j],A[i][j])
                if (j<(m-1)):
                    A[i][j]=max(temp[i][j+1],A[i][j])
        #temp=copy.deepcopy(A)
        temp=[]
        for i in range(n):
            temp.append([])
            for j in range(m):
                temp[i].append(A[i][j])
        
    return A

print(solve(2,[[8,5,4],[4,2,1]]))
                
