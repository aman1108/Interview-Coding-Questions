from collections import defaultdict

def solve(nums):
    n=len(nums)
    mv=max(nums)
    G=[0 for i in range(mv+1)]
    for x in nums:
        G[x]=G[x]+1

    H=defaultdict(lambda:0)
    for j in range(mv+1):
        if (G[j]!=0):
            H[G[j]]+=1

    ans=2

    for i in range(n-1,-1,-1):
        print(H)
        if (len(H)==2):
            a,b=H.keys()
            if((a==1 and H[a]==1) or (b==1 and H[b]==1)):
                return i+1

            if ((a-b==1 and H[a]==1) or (b-a==1 and H[b]==1)):
                return i+1

        elif(len(H)==1):
            a=0
            for b in H:
                a=b
            if (a==1 or H[a]==1):
                return i+1

        val=G[nums[i]]
        H[val]-=1
        if (H[val]==0):
            H.pop(val)
            
        G[nums[i]]-=1
        if (G[nums[i]]!=0):
            H[G[nums[i]]]+=1
        
#print(solve([2,2,1,1,5,3,3,5]))
#print(solve([1,1,1,2,2,2,3,3,3,4,4,4,5]))          
#print(solve([1,1,1,2,2,2]))
#print(solve([10,2,8,9,3,8,1,5,2,3,7,6]))                
#print(solve([50,50,50,50]))
#print(solve([50,50,50,70,70,70,20,20,20]))
print(solve([1,1,2,5,6,45,6,7]))
