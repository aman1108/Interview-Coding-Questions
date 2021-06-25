from collections import defaultdict
def solve(nums):
    G=defaultdict(list)

    for val in nums:
        cur=G
        flag=0
        for i in range(31,-1,-1):
            v=val&(1<<i)
            if (v>0):
                v=1
            if v in cur and flag==0:
                cur=cur[v]

            else:
                cur[v]=defaultdict(list)
                flag=1
                cur=cur[v]

    ans=0
    for val in nums:
        cur=G
        temp=0
        for i in range(31,-1,-1):
            v=val&(1<<i)
            if (v>0):
                v=1
            v=(v+1)%2
            if v in cur:
                cur=cur[v]
                temp=temp|(1<<i)

            else:
                v=(v+1)%2
                cur=cur[v]

        ans=max(ans,temp)
    return ans

print(solve([3,10,5,25,2,8]))
        


    
