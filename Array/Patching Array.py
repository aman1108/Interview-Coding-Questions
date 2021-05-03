def solve(nums,n):
    m=len(nums)
    ans=0
    cv=0
    i=0
    while(cv<n):
        
        if (i>=m):
            cv=cv+cv+1
            ans=ans+1
        elif ((cv+1)<nums[i]):
            cv=cv+cv+1
            ans=ans+1
        else:
            cv=cv+nums[i]
            i=i+1
    return ans

            
print(solve([1,3],6))
print(solve([1,5,10],20))
print(solve([1,2,2],5))
    
    
print(solve([1,2,31,33],2147483647))
