def solve(A):
    n=len(A)
    for i in range(n):
        count=0
        for j in range(n-i):
            if (j==i+j):
                continue
            if (A[j]==A[i+j]):
                count=count+1
        if (count>=2):
            return 1
    return 0

print(solve("aabb"))
