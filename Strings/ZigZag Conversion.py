def solve(s,numRows):
    if (len(s)<=numRows):
        return s
    ans=""
    a,b=(2*numRows)-2,0
    for i in range(numRows):
        ans=ans+s[i]
        ind=i
        while(ind<len(s)):
            ind=ind+a
            if (a>0 and ind<len(s)):
                  ans=ans+s[ind]
            ind=ind+b
            if (b>0 and ind<len(s)):
                  ans=ans+s[ind]
        a=a-2
        b=b+2
    return ans

print(solve("P",2))
              
             
        
