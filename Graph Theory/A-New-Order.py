def solve(n,A):

    Graph={}
    parent={}
    rank={}
    for i in range(n):
        for j in A[i]:
            Graph[j]=[]
            rank[j]=0
            
            
    for i in range(n-1):
        s1=A[i]
        s2=A[i+1]
        l=min(len(s1),len(s2))
        for j in range(l):
            if(s1[j]!=s2[j]):
                Graph[s1[j]].append(s2[j])
                parent[s2[j]]=s1[j]
                break

    #print(Graph,parent)
    rootnode=[]
    
    for i in Graph:
        if i not in parent:
            rootnode.append(i)

    mv=0
    for i in rootnode:
        Q=[i]
        while(len(Q)!=0):
            a=Q.pop()
            v=rank[a]
            for i in Graph[a]:
                rank[i]=max(v+1,rank[i])
                mv=max(mv,v+1)
                Q.append(i)

    ans=[[] for i in range(mv+1)]

    for i in rank:
        ans[rank[i]].append(i)

    for i in ans:
        i.sort()
        print(*i,sep="")
    
            
n=int(input())
A=[]
for i in range(n):
    A.append(input())

solve(n,A)
