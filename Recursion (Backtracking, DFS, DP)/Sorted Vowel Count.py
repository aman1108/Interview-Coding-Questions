def solve(n):
    ans=0
    def fun(ind,cl):
        nonlocal ans
        if (cl==n):
            ans=ans+1

        else:
            for i in range(ind,5):
                fun(i,cl+1)

    fun(0,0)
    return ans

print(solve(33))
        
