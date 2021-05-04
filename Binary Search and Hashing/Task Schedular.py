from collections import defaultdict
def solve(tasks,n):
    
    G=defaultdict(lambda:0)
    mv=0
    for i in range(len(tasks)):
        G[tasks[i]]+=1
        mv=max(mv,G[tasks[i]])

    cnt=0
    for i in G:
        if (G[i]==mv):
            cnt+=1

    #print(cnt,mv)
    ans=n*(mv-1)+mv    
    ans=ans+cnt-1
  
    return max(ans,len(tasks))


print(solve(["A","A","A","B","B","B"],0))
print(solve(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
print(solve(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2))
