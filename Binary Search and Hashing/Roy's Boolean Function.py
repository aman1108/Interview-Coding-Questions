mv=10
G={}
vis=[0 for i in range(mv+1)]
ans=[i for i in range(mv+1)]
for i in range(2,mv+1):
    if (vis[i]==0):
        j=i
        G[i]=1
        cnt=0
        while(j<=mv):
            vis[j]=1
            ans[j]=(ans[j]*(i-1))//i
            j=j+i
            cnt=cnt+1

#print(ans)
for _ in range(int(input())):
    N=int(input())
    val=ans[N]
    #print(val)
    if val in G:
        print("TRUE")
    else:
        print("FALSE")
