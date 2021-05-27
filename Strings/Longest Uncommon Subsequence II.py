from collections import defaultdict
def solve(strs):
    def issub(s1,s2):
        n=len(s1)
        m=len(s2)
        j=0
        for i in range(n):
            while (j<m and s1[i]!=s2[j]):
                j=j+1
            if(j==m):
                return 0
            j=j+1
        return 1

    
    strs.sort(reverse=True,key=lambda x:len(x))
    G=defaultdict(lambda:0)
    for v in strs:
        G[v]=G[v]+1
    n=len(strs)
    for i in range(n):
        flag=0
        if G[strs[i]]>1:
            continue
        for j in range(i-1):
            if (issub(strs[i],strs[j])==1):
                flag=1
                break
        
        if(flag==0):
            return len(strs[i])
    return -1

print(solve(["aba","aac","aae","aab","c"]))
