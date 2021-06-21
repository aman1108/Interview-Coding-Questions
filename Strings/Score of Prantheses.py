def solve(s):
    n=len(s)
    stk=[]
    ans=0

    for i in range(n):
        if (s[i]=="("):
            stk.append(ans)
        else:
            val=ans-stk.pop()
            if (val==0):
                ans=ans+1
            else:
                ans=ans+(val*2)-val
        

    return(ans)

print(solve("(()(()))"))
