import heapq
def solve(n,speed,efficiency,k):
    arr=[[efficiency[i],speed[i]] for i in range(n)]
    arr.sort()
    ans=0
    s=0
    pre=[0 for i in range(n-k+1)]
    A=[]
    for i in range(n-1,n-k-1,-1):
        A.append(arr[i][1])
        s+=arr[i][1]
        ans=max(ans,arr[i][0]*s)

    pre[n-k]=s
    heapq.heapify(A)
    for i in range(n-k-1,-1,-1):
        a=heapq.heappop(A)
        b=arr[i][1]
        pre[i]=s+b-a
        v=max(b,a)
        s=s+v-a
        heapq.heappush(A,v)

    
    for i in range(n-k+1):
        ans=max(ans,arr[i][0]*pre[i])
    return ans

print(solve(3,[2,8,2],[2,7,1],2))
        
