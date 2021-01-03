def solve(A):
    n=len(A)
    ans=float("inf")
    A.sort()
    for i in range(n-1):
        ans=min(ans,A[i]^A[i+1])
    return ans
#Can be solve using trie
print(solve([0,2,5,7]))
        
