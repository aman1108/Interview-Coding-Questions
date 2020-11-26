def solve(A):
    n=A
    s=""
    G={}
    for i in range(1,27):
        G[i%26]=chr(64+i)

    while(n!=0):
        v=n%26
        s=s+G[v]
        if(n%26==0):
            n=n-1
        n=n//26
        
    return (s[::-1])

print(solve(26))
        
        
        
