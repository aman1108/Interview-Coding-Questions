def solve(A,B):
    n=len(A)
    high=n-1
    low=0
    ans=0
    while(low<=high):
        #print(low,high)
        mid=(low+high)//2
        if (A[mid]>B):
            high=mid-1
        elif(A[mid]<B):
            ans=max(ans,mid)+1
            low=mid+1
        else:
            ans=max(ans,mid)+1
            low=mid+1
    return ans

print(solve([1,2,5,5],0))    
