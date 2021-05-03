from collections import defaultdict
def solve(S):
    n=len(S)
    G=defaultdict(lambda :0)
    for i in range(n):
        G[S[i]]=i

    cp=0
    cl=0
    i=0
    ans=[]
    while(i<n):
        cp=max(cp,G[S[i]])
        cl=cl+1
        if (i==cp):
            ans.append(cl)
            cl=0
        i=i+1
    return ans

print(solve("ababcbacadefegdehijhklij"))
print(solve("abcda"))
            
