def solve(tree):
    n=len(tree)
    v1,v2=-1,-1
    lind=0
    cnt=0
    ans=0
    for i in range(n):
        if (v1==-1):
            v1=tree[i]
            cnt=cnt+1
        
        elif (tree[i]!=v1 and v2==-1):
            v2=tree[i]
            cnt=cnt+1

        elif (v1!=-1 and v2!=-1 and tree[i]!=v1 and tree[i]!=v2):
            cnt=i-lind+1
            v1=tree[i-1]
            v2=tree[i]

        else:
            cnt=cnt+1

        if (i>0 and tree[i]!=tree[i-1]):
            lind=i
        #print(i,cnt,v1,v2,lind)
        ans=max(ans,cnt)

    return ans

print(solve([1,2,1]))
print(solve([1,2,3,2,2]))
print(solve([3,3,3,1,2,1,1,2,3,3,4]))
print(solve([0,1,6,6,4,4,6]))
