import math
def solve(x, y, N, R, A, B):
    DP=[[0 for i in range(y+1)] for j in range(x+1)]

    r=pow(R,2)
    for i in range(N):
        c1,c2=A[i],B[i]
        for j in range(x+1):
            for k in range(y+1):
                val=pow(j-c1,2)+pow(k-c2,2)
                if (val<=r):
                    DP[j][k]=1

    if(DP[0][0]==1):
        return ("NO")
                    
    #print(DP)      
    vis=[[0 for i in range(y+3)]for j in range(x+3)]

    print(DP)
    
    Q=[[0,0]]
    vis[0][0]=1
    while(len(Q)!=0 and vis[x][y]==0):
        print(Q)
        a,b=Q.pop()
        vis[a][b]=1
        pr1=[0,1,-1]
        pr2=[0,1,-1]
        for i in pr1:
            for j in pr2:
                #print(a,b,i,j)
                if (a+i>=0 and b+j>=0 and a+i<=x and b+j<=y and vis[a+i][b+j]==0 and DP[a+i][b+j]==0):
                    vis[a+i][b+j]=1
                    Q.append([a+i,b+j])
        
    flag=vis[x][y]
    if (flag==1):
        return ("YES")
    else:
        return ("NO")
        
     

                      
print(solve(5,5,2,1,[1,3],[3,3]))
