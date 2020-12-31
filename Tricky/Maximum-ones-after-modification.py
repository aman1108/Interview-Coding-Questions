def solve(A,B):
    k=B
    n=len(A)
    l=0
    ans=0
    cnt=0
    
    for i in range(n):
        if (A[i]==0):
            cnt=cnt+1

        if (cnt>k):
            if (A[l]==0):
                cnt=cnt-1
            l=l+1

        ans=max(ans,i-l+1)
    return ans
                


    
print(solve([1,0,0,1,1,0,1],2))
