def solve(nums1,nums2):
    n=len(nums1)
    arr=[[nums2[i],i] for i in range(n)]
    arr.sort(reverse=True)
    nums1.sort(reverse=True)

    print(arr,nums1)
    ans=[0]*n
    j=0
    k=1
    for i in range(n):
        while(j<n and nums1[i]<=arr[j][0]):
            ans[arr[j][1]]=nums1[-k]
            j=j+1
            k=k+1

        if(j>=n):
            break
        
        ans[arr[j][1]]=nums1[i]
        j=j+1
        
    return ans

print(solve([1,1,2],[1,2,1]))
