def solve(arr,n):
    cz=0
    co=0
    for i in range(n):
        if (arr[i]==1):
            cz=cz+1

        else:
            co=co+1
    A=[0]*co + [1]*cz
    return A

print(solve([1,0,1,1,0],5))
