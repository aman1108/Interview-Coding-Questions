def solve(nums1,nums2):
    def fun(l):
        p,mod=113,(10**9)+7
        pin=pow(p,mod-2,mod)
        pov=pow(p,l-1,mod)
        hashv=0
        G=set()
        for i in range(l):
            hashv=(hashv+(nums1[i]*pow(p,i,mod))%mod)%mod
        G.add(hashv)
        for i in range(l,len(nums1)):
            hashv=((hashv-nums1[i-l])*pin)%mod
            hashv=(hashv+(nums1[i]*pov)%mod)%mod
            G.add(hashv)

        
        hashv=0
        for i in range(l):
            hashv=(hashv+(nums2[i]*pow(p,i,mod))%mod)%mod
        if hashv in G:
            return True
        for i in range(l,len(nums2)):
            hashv=((hashv-nums2[i-l])*pin)%mod
            hashv=(hashv+(nums2[i]*pov)%mod)%mod
            if hashv in G:
                return True

            
    
    n=len(nums1)
    m=len(nums2)
    beg=0
    end=min(n,m)+1
    while(beg<end):
        l=(beg+end)//2
        if (fun(l)):
            beg=l+1
        else:
            end=l
    
    return beg-1

print(solve([0,0,0,0,0],[0,0,0,0,0]))
