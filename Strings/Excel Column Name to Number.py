def solve(A):
    s=A
    n=0
    G={}
    l=len(s)
    for i in range(1,27):
        G[chr(64+i)]=i

    for i in range(l):
        n=n+G[s[i]]*pow(26,l-i-1)

    return n

print(solve("A"))
