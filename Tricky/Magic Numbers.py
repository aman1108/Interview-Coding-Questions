arr=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
def fA(R,L,val):
    return ((R//val)-((L-1)//val))

T=int(input())
for _ in range(T):
    N,L,R=map(int,input().split())
    A=[]
    for i in arr:
        if (i>N):
            break
        A.append(i)
    ans=0
    pset=1<<len(A)
    print(A)
    for i in range(1,pset):
        p=1
        for j in range(len(A)):
            if (i &(1<<j)):
                p=p*A[j]

        
        if ((bin(i).count('1'))%2==0):
            ans=ans-fA(R,L,p)
        else:
            ans=ans+fA(R,L,p)
        #print(p,ans)
    print(ans)
        
        
