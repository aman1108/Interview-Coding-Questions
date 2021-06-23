def solve(height):
    n=len(height)
    beg=0
    end=n-1

    ans=0
    while(beg<end):
        v=min(height[beg],height[end])
        ans=max(ans,(end-beg)*v)
        if (v==height[beg]):
            beg=beg+1
        else:
            end=end-1
    return ans

print(solve([1,8,6,2,5,4,8,3,7]))
print(solve([1,1]))
print(solve([4,3,2,1,4]))
