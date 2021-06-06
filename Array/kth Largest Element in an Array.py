import random
def solve(nums,k):
    random.shuffle(nums)
    def fun(beg,end,nums):
        a=beg
        for i in range(beg+1,end+1):
            if (nums[i]<nums[a]):
                nums[i],nums[a+1]=nums[a+1],nums[i]
                nums[a],nums[a+1]=nums[a+1],nums[a]
                a=a+1
        return a
    
    n=len(nums)
    k=n-k
    beg=0
    end=n-1
    while(True):
        v=fun(beg,end,nums)
        #print(k,beg,end,v,nums)
        if (v==k):
            return nums[k]
        elif (v>k):
            end=v-1
        else:
            beg=v+1

print(solve([3,2,3,1,2,4,5,5,6],4))
