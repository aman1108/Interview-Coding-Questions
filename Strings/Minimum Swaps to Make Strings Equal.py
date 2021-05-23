def solve(s1,s2):
    n=len(s1)
    m=len(s2)

    x1=s1.count("x")
    x2=s2.count("x")

    if (n!=m or (x1+x2)%2!=0):
        return -1

    
    cnt1=0
    cnt2=0
    for i in range(n):
        if (s1[i]!=s2[i]):
            if (s1[i]=="x"):
                cnt1=cnt1+1
            else:
                cnt2=cnt2+1
    
    ans=(cnt1//2)+(cnt2//2)
    if (cnt1%2!=0):
        ans=ans+2
    return ans

print(solve("yyx","xxx"))
            
                            
                                
