from collections import defaultdict,deque
def solve(heights):
    n=len(heights)
    m=len(heights[0])

    def fun(n,m,heights,k):
        vis=[[0 for i in range(m)] for j in range(n)]
        Q=deque([[0,0]])

        while(len(Q)!=0):
            x,y=Q.popleft()
            vis[x][y]=1
            if (x==n-1 and y==m-1):
                return 1
            
            if (x>0 and vis[x-1][y]==0 and abs(heights[x-1][y]-heights[x][y])<=k):
                vis[x-1][y]=1
                Q.append([x-1,y])

            if (y>0 and vis[x][y-1]==0 and abs(heights[x][y-1]-heights[x][y])<=k):
                vis[x][y-1]=1
                Q.append([x,y-1])

            if (x<n-1 and vis[x+1][y]==0 and abs(heights[x+1][y]-heights[x][y])<=k):
                vis[x+1][y]=1
                Q.append([x+1,y])

            if (y<m-1 and vis[x][y+1]==0 and abs(heights[x][y+1]-heights[x][y])<=k):
                vis[x][y+1]=1
                Q.append([x,y+1])

        return 0

    
    low=0
    high=(10**6)+1
    ans=high

    while(low<=high):
        mid=(low+high)//2
        v=fun(n,m,heights,mid)
        if (v==1):
            ans=min(ans,mid)
            high=mid-1
        else:
            low=mid+1
    return ans

    ''' Dijskstra
    n=len(heights)
    m=len(heights[0])

    ans=0

    vis=[[0 for i in range(m)] for i in range(n)]
    Q=[[0,0,0]]
    heapq.heapify(Q)
    
    while(len(Q)):
        c,x,y=heapq.heappop(Q)
        ans=max(ans,c)
        if (vis[x][y]==0):
            vis[x][y]=1
            if (x==n-1 and y==m-1):
                return ans
            
            if (x>0 and vis[x-1][y]==0 ):
                heapq.heappush(Q,[abs(heights[x-1][y]-heights[x][y]),x-1,y])

            if (y>0 and vis[x][y-1]==0 ):
                heapq.heappush(Q,[abs(heights[x][y-1]-heights[x][y]),x,y-1])
                
            if (x<n-1 and vis[x+1][y]==0):
                heapq.heappush(Q,[abs(heights[x+1][y]-heights[x][y]),x+1,y])
                
            if (y<m-1 and vis[x][y+1]==0):
                heapq.heappush(Q,[abs(heights[x][y+1]-heights[x][y]),x,y+1])
    '''

print(solve([[1,2,2],[3,8,2],[5,3,5]]))
print(solve([[1,2,3],[3,8,4],[5,3,5]]))
print(solve([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
