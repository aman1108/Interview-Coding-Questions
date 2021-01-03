#https://www.interviewbit.com/problems/count-total-set-bits/
def solve(A):
    n=A
    m=len(bin(n))-2
    ans=0
    mod=(10**9)+7
    for i in range(m):
        v=pow(2,i)
        x=(n+1)//v
        #print(i,ans)
        ans=(ans+((x//2)*v)%mod)%mod
        if (x%2!=0):
            ans=(ans+((n+1)%v)%mod)%mod
    return ans%mod

print(solve(10))
            
'''c=0    
for i in range(11):
    c=c+bin(i).count("1")

print(c)'''
    
