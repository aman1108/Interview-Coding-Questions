def solve(graph):
    def dfs(graph,ans,path,node):
        path.append(node)
        if (node==len(graph)-1):
            ans.append(path.copy())
        else:
            for val in graph[node]:
                dfs(graph,ans,path,val)

        path.pop()

    ans=[]
    dfs(graph,ans,[],0)
    return ans

print(solve([[1,2],[3],[3],[]]))
print(solve([[1,2,3],[2],[3],[]]))
print(solve([[1],[]]))
print(solve([[1,3],[2],[3],[]]))
