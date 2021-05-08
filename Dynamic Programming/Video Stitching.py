from collections import defaultdict
def solve(clips,T):
    G=[0]*(T+1)
    for a,b in clips:
        if (a<T):
            G[a]=max(G[a],b)


    cur=G[0]
    net=0
    i=0
    cnt=1
    while(i<=T):
        #print(cur,i)
        if (cur>=T):
            return cnt
        
        if(cur<=i):
            return -1
        
        j=i
        while(j<=cur):
            net=max(net,G[j])
            j=j+1
            
        i=j
        cur=net
        cnt=cnt+1
        
    return cnt
        

    ''' DP
    n=len(clips)
    clips.sort(key=lambda x:[x[0],-x[1]])

    DP=[10**9]*(T+1)
    DP[0]=0

    for i in range(n):
        v=clips[i][0]
        for j in range(clips[i][0]+1,min(clips[i][1]+1,T+1)):
            DP[j]=min(DP[j],1+DP[v])
        
    if(DP[T]==10**9):
        return -1

    return DP[-1]'''


print(solve([[2,4]],0))
print(solve([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]],10))
    
print(solve([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9))

print(solve([[0,1],[1,2]],5))

print(solve([[0,4],[2,8],[5,7]],5))

print(solve([[0,2],[1,6],[3,10]],10))
