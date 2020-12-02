def solve(A,B,C,D):
    if(D==0):
        return []
    s=[A,B,C]
    ia=[0,0,0]
    ans=[min(s)]
    while(len(ans)!=D):
        m=min(s)
        if(m!=ans[-1]):
            ans.append(m)
        
        if(m==s[0]):
            s[0]=ans[ia[0]]*A
            ia[0]=ia[0]+1

        elif(m==s[1]):
            s[1]=ans[ia[1]]*B
            ia[1]=ia[1]+1

        else:
            s[2]=ans[ia[2]]*C
            ia[2]=ia[2]+1
    
    return ans

print(solve(3,11,7,50))
    
