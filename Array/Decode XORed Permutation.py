def solve(encoded):
    n=len(encoded)
    v=0
    for i in range(1,n+2):
        v=v^i

    for i in range(1,n,2):
        v=v^encoded[i]

    ans=[v]
    for i in range(n):
        ans.append(encoded[i]^ans[-1])

    return ans

print(solve([6,5,4,6]))
        
