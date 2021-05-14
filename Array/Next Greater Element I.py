from collections import defaultdict
def solve(nums1,nums2):
    m=len(nums2)

    stk=[]
    G=defaultdict(lambda:-1)
    for i in range(m-1,-1,-1):
        print(stk)
        while(len(stk)>0 and stk[-1]<nums2[i]):
            stk.pop()
        if (len(stk)>0):
            G[nums2[i]]=stk[-1]
        stk.append(nums2[i])

   
    result=[]
    for v in nums1:
        result.append(G[v])

    return result

print(solve([2,4],[1,2,3,4]))
