def pow(self, x, n, d):
        ans=1
        x=x%d
        if (x==0):
            return x
        while (n>0):
            if (n&1==1):
                ans=(ans*x)%d
            n=n>>1
            x=(x*x)%d
        return ans
