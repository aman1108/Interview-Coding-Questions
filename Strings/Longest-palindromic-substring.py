''' O(n^2) Time and O(n^2) Space
def solve(s):
        n=len(s)
        DP=[[-1 for i in range(n)] for j in range(n)]
        ans=0
        x,y=0,0
        for j in range(n):
            for i in range(j,-1,-1):
                if (i==j):
                    DP[i][j]=1

                elif (j==i+1 and s[i]==s[j]):
                    DP[i][j]=2
                    
                elif (s[i]==s[j] and DP[i+1][j-1]!=-1):
                    DP[i][j]=DP[i+1][j-1]+2

                if (DP[i][j]>ans):
                    ans=DP[i][j]
                    x,y=i,j
        #print(DP)
        return s[x:y+1]'''

def solve(s):
    n=len(s)
    ans=1
    st=s[0]
    for i in range(n):
        l=i-1
        r=i+1
        cl=1
        while(l>=0 and r<n):
            if (s[l]==s[r]):
                cl=cl+2
                l=l-1
                r=r+1
            else:
                break
        if (cl>ans):
            st=s[l+1:r]
            ans=cl

    for i in range(n-1):
        if (s[i]==s[i+1]):
            cl=2
            l=i-1
            r=i+2
            while(l>=0 and r<n):
                if (s[l]==s[r]):
                    cl=cl+2
                    l=l-1
                    r=r+1
                else:
                    break
            if (cl>ans):
                st=s[l+1:r]
                ans=cl
    return st

print(solve("abcba"))

        
        
        
