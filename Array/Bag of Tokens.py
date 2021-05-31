def solve(tokens, power):
    n=len(tokens)
    tokens.sort()
    i=0
    j=n-1
    sc=0
    ans=0
    while(i<=j):
        flag=0
        while(i<=j and tokens[i]<=power):
            power=power-tokens[i]
            i=i+1
            flag=1
            sc=sc+1

        ans=max(ans,sc)
        if (sc>0 and i<j):
            power=power+tokens[j]
            j=j-1
            flag=1
            sc=sc-1
        if(flag==0):
            return ans
    return ans

print(solve([40],50))
print(solve([100,200],150))
print(solve([100,200,300,400],200))
