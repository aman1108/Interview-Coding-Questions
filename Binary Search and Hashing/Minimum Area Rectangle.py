from collections import defaultdict
def solve(points):
    G=defaultdict(list)
    for x,y in points:
        G[x].append(y)

    L={}
    ans=10**9
    for val in sorted(G):
        col=G[val]
        col.sort()
        for i in range(len(col)):
            for j in range(i+1,len(col)):
                if (col[i],col[j]) in L:
                    ans=min(ans,(val-L[col[i],col[j]])*(col[j]-col[i]))
                L[col[i],col[j]]=val

    return ans%(10**9)

print(solve([[1,1],[1,3],[3,1],[3,3],[2,2]]))
                
print(solve([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))

print(solve([[1,3],[2,1],[2,0],[4,3],[0,4],[4,2],[1,0],[3,4],[2,4],[4,0]]))
