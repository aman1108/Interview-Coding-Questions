def solve(asteroids):
    n=len(asteroids)
    stk=[]
    ans=[]
    vis=[0]*n
    for i in range(n):
        if (asteroids[i]<0):
            asteroids[i]=abs(asteroids[i])
            while(len(stk)>0 and asteroids[stk[-1]]<asteroids[i]):
                stk.pop()
            if (len(stk)==0):
                vis[i]=1

            elif (asteroids[stk[-1]]==asteroids[i]):
                stk.pop()
            asteroids[i]=-1*asteroids[i]
        else:
            stk.append(i)

    for v in stk:
        vis[v]=1

    ans=[]
    for i in range(n):
        if (vis[i]==1):
            ans.append(asteroids[i])
    return ans

print(solve([8,-8]))
print(solve([10,2,-5]))
print(solve([-2,-1,1,2]))
