from collections import defaultdict
def solve(A):
    n=len(A)
    m=len(A[0])

    g=[]
    for i in A:
        for j in i:
            g.append(j)
    g.sort(reverse=True)
    ans=[0,0,0]
    for val in g:
        if (ans[0]<val and val not in ans):
                ans[0]=val
                ans.sort()
        
    DP=[[[0,0,0,0] for i in range(m)] for j in range(n)]
    for i in range(min(n,m)):
        for j in range(n):
            for k in range(m):
                x,y=j,k
                val=0
                if (x+i<=(n-1) and (y-i)>=0):
                    DP[x][y][0]+=A[x+i][y-i]
                    val=val+DP[x][y][0]-A[x][y]
                    x=x+i
                    y=y-i
                else:
                    continue

                if (x+i<=(n-1) and (y+i)<=(m-1)):
                    DP[x][y][1]+=A[x+i][y+i]
                    val=val+DP[x][y][1]-A[x][y]
                    x=x+i
                    y=y+i
                else:
                    continue

                if (x-i<=(n-1) and (y+i)<=(m-1)):
                    DP[x][y][2]+=A[x-i][y+i]
                    val=val+DP[x][y][2]-A[x][y]
                    x=x-i
                    y=y+i
                else:
                    continue

                if (x-i<=(n-1) and (y-i)<=(m-1)):
                    DP[x][y][3]+=A[x-i][y-i]
                    val=val+DP[x][y][3]-A[x][y]
                    x=x-i
                    y=y-i
                else:
                    continue
                #print(i,j,k,val)
                if (ans[0]<val and val not in ans):
                    ans[0]=val
                    ans.sort()
    
    ans.reverse()
    fa=[]
    for i in ans:
        if i==0:
            return fa
        fa.append(i)
    return ans  

print(solve([[7],[7],[7]]))   
#print(solve([[7,7,7]]))
#print(solve([[1,2,3],[4,5,6],[7,8,9]]))
#print(solve([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]))
