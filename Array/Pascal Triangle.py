def solve(A):
    if (A==0):
        return []
    
    ans=[[1]]
    for i in range(A-1):
        temp=[1]
        a=ans[-1]
        for i in range(1,len(a)):
            v=a[i]+a[i-1]
            temp.append(v)
        temp.append(1)
        ans.append(temp)

    return ans

print(solve(5))
