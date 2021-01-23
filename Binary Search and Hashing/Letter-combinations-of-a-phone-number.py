def solve(digits):
        n=len(digits)
        if (n==0):
            return []
        G={}
        G['2']=['a','b','c']
        G['3']=['d','e','f']
        G['4']=['g','h','i']
        G['5']=['j','k','l']
        G['6']=['m','n','o']
        G['7']=['p','q','r','s']
        G['8']=['t','u','v']
        G['9']=['w','x','y','z']
        A=[]
        for i in digits:
            A.append(G[i])

        ans=A[0]
        for i in range(1,n):
            B=A[i]
            C=[]
            for j in range(len(ans)):
                for k in range(len(B)):
                    v=ans[j]+B[k]
                    C.append(v)
            ans=C
        return ans
           
         
print(solve("23"))
        
