def solve(A):
    n=A
    if (n<=2):
        return n

    a,b=1,2
    ans=0
    for i in range(n-2):
        c=a+b
        ans=c
        a,b=b,c

    return ans

print(solve(4))
