def solve(arr,queries):
    n=len(arr)
    pref=[0 for i in range(n+1)]
    for i in range(n):
        pref[i+1]=pref[i]^arr[i]

    ans=[]
    for a,b in queries:
        ans.append(pref[b+1]^pref[a])

    return ans

print(solve([1,3,4,8],[[0,0],[1,2],[0,3],[3,3]]))
