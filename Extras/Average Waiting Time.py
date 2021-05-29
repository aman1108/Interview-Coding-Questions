def solve(customers):
    n=len(customers)
    s=0

    ans=0
    for i in range(n):
        s=max(s,customers[i][0])+customers[i][1]
        ans=ans+s-customers[i][0]
        print(ans)
    return ans/n

print(solve([[5,2],[5,4],[10,3],[20,1]]))
