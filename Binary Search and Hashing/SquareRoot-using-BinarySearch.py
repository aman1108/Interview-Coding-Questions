
def solve(A):
    #A>>1 will directly give ouput
    if (A==0 or A==1):
        return A
    n=A
    low=0
    high=A
    ans=1
    while(low<=high):
        print(low,high)
        mid=(low+high)//2
        v=pow(mid,2)
        
        if (v>n):
            high=mid-1

        elif(v<n):
            ans=mid
            low=mid+1

        else:
            return mid

    return ans

print(solve(6))
    
