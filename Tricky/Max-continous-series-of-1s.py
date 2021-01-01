#https://www.interviewbit.com/problems/max-continuous-series-of-1s/
def solve(A,B):
    k=B
    n=len(A)
    l=0
    ans=0
    cnt=0

    fl=0
    fr=0
    for i in range(n):
        if (A[i]==0):
            cnt=cnt+1

        if (cnt>k):
            if (A[l]==0):
                cnt=cnt-1
            l=l+1

        #print(l,ans)
        if (ans<i-l+1):
            ans=i-l+1
            fl=l
            fr=i

    A1=[]
    
    for i in range(fl,fr+1):
        A1.append(i)
    return A1
                


    
print(solve([1,1,0,1,1,0,0,1,1,1],1))
