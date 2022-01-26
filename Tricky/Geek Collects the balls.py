def solve(n,m,A,B):
    i=0
    j=0
    val1,val2=0,0
    x,y=0,0
    while(i<n and j<m):
        x,y=A[i],B[j]
        if (x<y):
            val1=val1+x
            i=i+1

        elif(y<x):
            val2=val2+y
            j=j+1
            
        else:
            x1,y1=0,0
            while(i<n and A[i]==x):
                x1=x1+x
                i=i+1
            while(j<m and B[j]==y):
                y1=y1+y
                j=j+1

            val1,val2=max(val1+x1,val1+x1+y1-(2*x),val2+x1+y1-x),max(val2+y1,val2+x1+y1-(2*x),val1+x1+y1-x)
        print(i,j,val1,val2)
    while(i<n):
        val1=val1+A[i]
        i=i+1
    while(j<m):
        val2=val2+B[j]
        j=j+1
    ans=max(val1,val2)
    return ans

#print(solve(5,5,[1,4,5,6,8],[2,3,4,6,9]))
#print(solve(6,5,[1,4,5,8,8,8],[2,8,9,9,9]))
#print(solve(3,3,[1,2,3],[4,5,6]))
print(solve(7,7,[4,5,6,7,8,8,9],[1,1,8,8,8,8,8]))
            
