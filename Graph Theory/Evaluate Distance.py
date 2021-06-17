from collections import defaultdict,deque
def solve(equations,values,queries):

    def bfs(graph,a,b):
        s=defaultdict(lambda :[-1,1])
        Q=deque([a])
        s[a][0]=0
        while(len(Q)):
            n1=Q.popleft()
            if (n1==b):
                ans=1
                while(n1!=a):
                    ans=ans*s[n1][1]
                    n1=s[n1][0]
                return ans
                
            for n2,val in graph[n1]:
                if (s[n2][0]==-1):
                    s[n2]=[n1,val]
                    Q.append(n2)
        return -1
    
    n=len(equations)
    G=defaultdict(list)

    ele=set()
    for i in range(n):
        a,b=equations[i]
        G[a].append([b,values[i]])
        G[b].append([a,1/values[i]])
        ele.add(a)
        ele.add(b)

    
    ans=[]
    for a,b in queries:
        if a in ele and b in ele:
            ans.append(bfs(G,a,b))
        else:
            ans.append(-1)
    return ans

#print(solve([["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))

print(solve([["a","e"],["b","e"]],
[4.0,3.0],
[["a","b"],["e","e"],["x","x"]]))
        
