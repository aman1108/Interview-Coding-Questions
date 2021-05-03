def solve(nums):
    ans=[]
    for i in range(len(nums)):
        v=abs(nums[i])
        nums[v-1]=-1*(abs(nums[v-1]))

    for i in range(len(nums)):
        if (nums[i]>0):
            ans.append(i+1)

    return ans

print(solve([4,3,2,7,8,2,3,1]))
print(solve([1,1]))
                    
                    
