def solve(arr):
    n=len(arr)
    mod=(10**9)+7
    left=[1]*(n)
    ans=0
    stk=[]
    for i in range(n):
        while(len(stk)>0 and arr[stk[-1]]>arr[i]):
            stk.pop()

        if (len(stk)>0):
            left[i]=i-stk[-1]
        else:
            left[i]=i+1
        stk.append(i)

    stk=[]
    for i in range(n-1,-1,-1):
        while(len(stk)>0 and arr[stk[-1]]>=arr[i]):
            stk.pop()
        
        if (len(stk)>0):
            ans=(ans+((arr[i]*(stk[-1]-i)*left[i]))%mod)%mod
        else:
            ans=(ans+(arr[i]*(n-i)*left[i])%mod)%mod
        stk.append(i)

    return ans

#print(solve([3,1,2,4]))
#print(solve([11,81,94,43,3]))
print(solve([11,81,94,43,3,3,1,2,4]))
