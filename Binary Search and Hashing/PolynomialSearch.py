def rval(A,B,C,x):
    return ((A*x*x)+(B*x)+C)

for _ in range(int(input())):
    A,B,C,K=map(int,input().split())
    low=0
    high=(10**5)+1
    ans=high
    while(low<=high):
        mid=(low+high)//2
        val=rval(A,B,C,mid)
        print(low,high,mid,val)
        if (val<K):
            low=mid+1
        else:
            ans=min(ans,mid)
            high=mid-1
    print(ans)
            
            
