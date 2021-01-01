def solve(A):
    n=len(A)
    G={}

    for i in range(n):
        B=[0 for j in range(26)]
        s=A[i]
        for j in s:
            B[ord(j)-97]=B[ord(j)-97]+1
        v=""
        for j in B:
            v=v+str(j)+"+"

        if v in G:
            G[v].append(i+1)
        else:
            G[v]=[i+1]
    A=[]
    for i in G:
        A.append(G[i])
    return A

print(solve(["cat","dog","god","tca"]))
        
