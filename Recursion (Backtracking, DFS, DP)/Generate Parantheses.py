def solve(n):
    ans=[]
    def fun(n,string,ct1,ct2):
        if (ct1==n and ct2==n):
            ans.append(string)
            return
        
        if (ct1!=n):
            new=string+"("
            fun(n,new,ct1+1,ct2)
        
        if(ct2<ct1):
            new=string+")"
            fun(n,new,ct1,ct2+1)

    fun(n,"",0,0)
    return ans

print(solve(1))
        
