#https://www.interviewbit.com/problems/array-3-pointers/
def solve(A,B,C):
    n=len(A)
    m=len(B)
    p=len(C)

    i=0
    j=0
    k=0

    ans=float("inf")
    while(i<n and j<m and k<p):
        a,b,c=A[i],B[j],C[k]
        mv=min(a,b,c)
        vm=max(a,b,c)

        ans=min(ans,vm-mv)

        if (mv==a):
            i=i+1

        elif(mv==b):
            j=j+1

        else:
            k=k+1

    return ans


        
        
