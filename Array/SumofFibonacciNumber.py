#https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/
def fibsum(A):
    n=A
    A=[1,2]
    i=1
    j=2
    while((i+j)<=n):
        i,j=j,i+j
        A.append(j)

    ans=0
    i=len(A)-1
    while(n>0):
        while((n-A[i])>=0):
            n=n-A[i]
            ans=ans+1
        i=i-1
    return ans

print(fibsum(7))
    
            
