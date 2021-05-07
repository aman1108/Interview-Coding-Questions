def solve(numss):
    n=len(nums)
    i=n-1
    while(i>0):
        if (nums[i]>nums[i-1]):
            for j in range(n-1,i-1,-1):
                if (nums[j]>nums[i-1]):
                    nums[i-1],nums[j]=nums[j],nums[i-1]
                    break

            left=i
            right=n-1
            while(left<right):
                nums[left],nums[right]=nums[right],nums[left]
                left=left+1
                right=right-1

            return 
        i=i-1

    nums.reverse()
        
        
    

print(solve([5,4,8,9,3,5,5,2,4,1]))
