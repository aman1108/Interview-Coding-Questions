def partition(s):
    n=len(s)
    ans=[]
    par=[]

    def dfs(i):
        if (i>=n):
            ans.append(par.copy())

        for j in range(i,n):
            if (ckpalin(s,i,j)==1):
                par.append(s[i:j+1])
                dfs(j+1)
                par.pop()
    
    
    def ckpalin(s,i,j):
        while(i<j):
            if (s[i]==s[j]):
                i=i+1
                j=j-1
            else:
                return 0
        return 1

    dfs(0)
    return ans

print(partition("aab"))
            
