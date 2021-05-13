def solve(price,special,needs):
    n=len(price)
    m=len(special)
    ans=0
    G={}
    for i in range(n):
        ans=ans+(price[i]*needs[i])
    def fun(n,m,price,special,needs,val):
        nonlocal ans
        if tuple(needs) in G:
            ans=min(ans,val+G[tuple(needs)])
            return G[tuple(needs)]
        
        if (sum(needs)==0):
            ans=min(ans,val)
            return 0

        tval=0
        for i in range(n):
            tval=tval+(price[i]*needs[i])
        arr=[tval]
        
        for j in range(m):
            temp=[]
            flag=0
            for k in range(n):
                if (needs[k]-special[j][k]>=0):
                    temp.append(needs[k]-special[j][k])
                else:
                    flag=1
                    break
            if(flag==0):
                val1=fun(n,m,price,special,temp,val+special[j][-1])
                arr.append(special[j][-1]+val1)
        v=min(arr)
        ans=min(ans,val+v)
        #print(needs,v)
        return v
    
    fun(n,m,price,special,needs,0)
    return ans

print(solve([2,5],[],[3,2]))
print(solve([2,3,4],[[1,1,0,4],[2,2,1,9]],[1,2,1]))
