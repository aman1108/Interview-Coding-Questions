def solve(A,B):
    n=len(A)    
    x,y=0,1
    for i in range(n-2,-1,-1):
        tx,ty=10**9,10**9
        if (A[i]<A[i+1] and B[i]<B[i+1]):
            tx=min(tx,x)
            ty=min(ty,1+y)

        if (A[i]<B[i+1] and B[i]<A[i+1]):
            tx=min(tx,y)
            ty=min(ty,1+x)
        x,y=tx,ty
        #print(x,y)

    return min(tx,ty)

#print(solve([1,3,3,4],[1,2,5,7]))
print(solve([0,4,4,5,9],[0,1,6,8,10]))
