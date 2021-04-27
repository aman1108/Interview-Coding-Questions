def solve(arr):
        n=len(arr)
        ans=1
        cnt=0
        for i in range(1,n):
            if (i==n-1):
                if (arr[i]!=arr[i-1]):
                    ans=max(ans,2)
                break
            if ((arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (arr[i]<arr[i-1] and arr[i]<arr[i+1])):
                if (cnt==0):
                    cnt=2
                cnt=cnt+1

            else:
                cnt=0
            if (arr[i]!=arr[i-1]):
                ans=max(ans,2)
            ans=max(ans,cnt)

        return ans

print(solve([9,4,2,10,7,8,8,1,6]))
print(solve([1,1,1,1]))
print(solve([4,8,12,16]))
        
