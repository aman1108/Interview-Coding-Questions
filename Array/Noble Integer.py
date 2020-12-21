def solve(A):
    n=len(A)
    A.sort()
    A.append(-1)
    i=0
    while(i<n):
        while(A[i]==A[i+1]):
            i=i+1
        if ((n-i-1)==A[i]):
            return 1
        i=i+1
    return -1
        
print(solve([3,3,1,1]))
