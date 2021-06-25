def solve(nums):
    s=set()

    mask=0
    ans=0
    for i in range(30,-1,-1):
        mask=ans|(1<<i)
        for val in nums:
            s.add(val&mask)

        for val in nums:
            if (val&mask)^mask in s:
                ans=mask
                break
        s.clear()
    return ans

print(solve([3,10,5,25,2,8]))
        
