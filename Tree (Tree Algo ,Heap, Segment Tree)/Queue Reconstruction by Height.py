import math
def solve(people):
    def construct(val,segT,arr):
        for i in range(val):
            segT[val+i]=arr[i]

        for i in range(val-1,0,-1):
            segT[i]=segT[2*i]+segT[(2*i)+1]
        
    def find(segT,val,l,r):
        l=l+val
        r=r+val
        ans=0
        while(l<r):
            if (l%2!=0):
                ans=ans+segT[l]
                l=l+1
            if(r%2==0):
                ans=ans+segT[r]
                r=r-1
            l=l//2
            r=r//2
        if (l==r):
            ans=ans+segT[l]
        return ans

    def update(segT,val,ind,v):
        ind=ind+val
        segT[ind]=v
        ind=ind//2
        while(ind!=0):
            segT[ind]=segT[(2*ind)]+segT[(2*ind)+1]
            ind=ind//2
        
    
    n=len(people)
    people.sort(key= lambda x:[x[0],-1*x[1]])
    
    result=[[] for i in range(n)]
    val=pow(2,math.ceil(math.log2(n)))
    arr=[1]*n+[0]*(val-n)
    segT=[0]*2*val
    construct(val,segT,arr)
    
    for i in range(n):
        x=people[i][1]+1
        beg=0
        end=n-1
        ans=n-1
        while(beg<=end):
            mid=(beg+end)//2
            v=find(segT,val,0,mid)
            #print(beg,end,mid,v)
            if(v>x):
                end=mid-1
            elif(v<x):
                beg=mid+1
            else:
                ans=min(ans,mid)
                end=mid-1
            
        #print(x,ans)
        result[ans]=people[i]
        update(segT,val,ans,0)
    return result

people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people=[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(solve(people))
