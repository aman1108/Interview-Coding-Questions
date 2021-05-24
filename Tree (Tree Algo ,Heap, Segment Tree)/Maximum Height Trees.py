from collections import defaultdict, deque
def solve(n,edges):
    G=defaultdict(list)
    cnt=[0]*n
    for a,b in edges:
        G[a].append(b)
        G[b].append(a)
        cnt[a]+=1
        cnt[b]+=1

    arr=[]
    vis=[0]*n
    for i in G:
        if (len(G[i])==1):
            vis[i]=1
            arr.append(i)

    while(len(arr)!=0):
        temp=[]
        for a in arr:
            for b in G[a]:
                if (vis[b]==0):
                    if (cnt[b]==2):
                        temp.append(b)
                        cnt[b]=0
                    else:
                        cnt[b]=cnt[b]-1
        #print(arr,temp)
        if(len(temp)==0):
            return arr
        arr=temp
    return [0]

print(solve(4,[[1,0],[1,2],[1,3]]))
            
print(solve(7,[[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]))
