def solve(A):
    n=len(A)
    marr=[A[0]]
    mv=A[0]
    for i in range(1,n):
        marr.append(mv)
        mv=max(mv,A[i])

    arr=[0 for i in range(n)]
    arr[-1]=A[-1]
    mv=A[-1]

    for i in range(n-2,-1,-1):
        arr[i]=mv
        mv=min(A[i],mv)

    for i in range(1,n-1):
        if(A[i]>marr[i] and A[i]<arr[i]):
            return 1

    return 0

print(solve([5,1,4,4]))

print(solve([ 9895, 30334, 17674, 23812, 20038, 25668, 6869, 1870, 4665, 27645, 7712, 17036, 31323, 8724, 28254, 28704, 26300, 25548, 15142, 12860, 19913, 32663, 32758 ]))
