def solve(A):
    n=A
    A=[[0 for i in range(n)] for j in range(n)]

    l,r,u,d=0,n,n,-1
    f=0
    x,y=0,0

    cnt=0
    while(cnt<(n*n)):
        i=cnt
        if (f==0 and y>=u):
            u=u-1
            f=1
            x=x+1
            y=u

        elif(f==0 and y<u):
            A[x][y]=i+1
            y=y+1
            cnt=cnt+1

        elif(f==1 and x>=r):
            r=r-1
            f=2
            y=y-1
            x=r
            
        elif(f==1 and x<r):
            A[x][y]=i+1
            x=x+1
            cnt=cnt+1

        
        elif(f==2 and y<=d):
            d=d+1
            f=3
            x=x-1
            y=d
            
        elif(f==2 and y>d):
            A[x][y]=i+1
            y=y-1
            cnt=cnt+1

        
        elif(f==3 and x<=l):
            l=l+1
            f=0
            y=y+1
            x=l
            
        elif(f==3 and x>l):
            A[x][y]=i+1
            x=x-1
            cnt=cnt+1

        
    return A

print(solve(2))
        
        

        
    
    
