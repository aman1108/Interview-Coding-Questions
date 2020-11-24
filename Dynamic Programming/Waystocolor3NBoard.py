A=int(input())
mod=(10**9)+7
clr1,clr2=24,12

for i in range(2,A+1):
    clr1,clr2=(11*clr1+10*clr2)%mod,(5*clr1+7*clr2)%mod

print((clr1+clr2)%mod)
     
