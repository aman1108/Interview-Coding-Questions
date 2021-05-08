def solve(arr,k):
    mod=(10**9)+7
    s=max(sum(arr),0)
    if (k==1):
        n=len(arr)
        val=0
        ans=0
        for i in range(n):
            val=max(arr[i],val+arr[i])
            ans=max(ans,val)
        return ans%mod
    else:
        arr=arr+arr
        n=len(arr)
        val=0
        ans=0
        for i in range(n):
            val=max(arr[i],val+arr[i])
            ans=max(ans,val)
        
            
        ans=ans%mod
        ans=(ans+((k-2)*s)%mod)%mod
        return ans

    
print(solve([4,-10,-2,-3,4],1))
        

        
