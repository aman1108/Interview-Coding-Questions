def solve(nums):
    n=len(nums)
    ans=[1]*n

    st=1
    for i in range(n):
        ans[i]=ans[i]*st
        st=st*nums[i]

    st=1
    for i in range(n-1,-1,-1):
        ans[i]=ans[i]*st
        st=st*nums[i]

    return ans

print(solve([-1,1,0,-3,3]))
