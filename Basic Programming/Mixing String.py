from itertools import permutations  
  
def merge(A,B):
    C=A
    G={}
    s=""
    for i in B:
        s=s+i
        G[s]=1
    for i in range(len(A)):
        if A[i:] in G:
            return A[:i]+B
    return A+B

def fA(n,A):
    s=A[0]
    for i in range(1,n):
        s=(merge(s,A[i]))
    #print(A,s)
    return len(s)
        
        
N=int(input())
A=[]
for _ in range(N):
    A.append(input())

perm = permutations(A)
ans=float("inf")
for val in perm:
    
    ans=min(ans,fA(N,val))
print(ans)
