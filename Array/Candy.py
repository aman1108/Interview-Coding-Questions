def solve(ratings):
    n=len(ratings)
    vis=[1 for i in range(n)]
    vis1=[1 for i in range(n)]
    for i in range(1,n):
        if (ratings[i]>ratings[i-1]):
            vis[i]=vis[i-1]+1

    for i in range(n-2,-1,-1):
        if (ratings[i]>ratings[i+1]):
            vis1[i]=vis1[i+1]+1

    ans=[max(vis[i],vis1[i]) for i in range(n)]
            
    return sum(ans)

print(solve([1,2,2]))
print(solve([1,2,87,87,87,2,1]))         
print(solve([29,51,87,87,72,12]))
print(solve([1,3,4,5,2]))
