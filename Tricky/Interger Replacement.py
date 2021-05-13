def solve(n):
    ans=0
    while(n!=1):
        if (n%2==0):
            n=n//2
        elif (n%4==1 or n==3):
            n=n-1
        else:
            n=n+1
        ans=ans+1
        
    return ans

print(solve(3))
