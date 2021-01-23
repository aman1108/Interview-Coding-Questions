def solve(s):
        n=len(s)
        ans=0
        val=0
        G={}
        for i in range(n):
            if s[i] not in G:
                G[s[i]]=i
            else:
                val=max(G.pop(s[i])+1,val)
                G[s[i]]=i
            ans=max(ans,i-val+1)
        return ans


print(solve("abba"))
        
