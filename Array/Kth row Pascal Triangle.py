def solve(A):
    ans=[1]
    for i in range(A):
        temp=[1]
        for i in range(1,len(ans)):
            v=ans[i]+ans[i-1]
            temp.append(v)
        temp.append(1)
        ans=temp

    return ans

print(solve(5))
