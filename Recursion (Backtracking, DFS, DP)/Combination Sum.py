def solve(candidates,target):
    n=len(candidates)
    ans=[]
    def solve(x,target,path,beg):
        if (x==target):
            ans.append(path.copy())
        for i in range(beg,n):
            if (x+candidates[i]<=target):
                path.append(candidates[i])
                solve(x+candidates[i],target,path,i)
                path.pop()
                
    solve(0,target,[],0)
    return ans

print(solve([2,3,6,7],7))
