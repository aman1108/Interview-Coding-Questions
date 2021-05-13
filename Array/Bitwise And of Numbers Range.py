def solve(m,n):
    ans=0
    while(m!=0 and n!=0):
        x=len(bin(m))-2
        y=len(bin(n))-2
        if (x!=y):
            return ans
        val=pow(2,x-1)
        ans=ans+val
        m=m-val
        n=n-val
    return ans

print(solve(0,1))
