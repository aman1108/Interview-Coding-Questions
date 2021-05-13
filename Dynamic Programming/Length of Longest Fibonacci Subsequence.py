from collections import defaultdict
def solve(arr):
    n=len(arr)
    ans=0
    G=defaultdict(lambda:0)
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if (arr[j],arr[i]+arr[j]) in G:
                G[arr[i],arr[j]]=max(G[arr[i],arr[j]],1+G[(arr[j],arr[i]+arr[j])])
                ans=max(ans,G[arr[i],arr[j]])
            else:
                G[arr[i],arr[j]]=max(G[arr[i],arr[j]],2)
        #print(G)
    return ans
            



    
print(solve([1,2,3,4,5,6,7,8]))
print(solve([1,3,7,11,12,14,18]))

print(solve([2,3,4,5,7,11]))
