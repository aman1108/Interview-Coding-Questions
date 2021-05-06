def solve(S):
    n=len(S)
    ans=['']
    for i in range(n):
        if (S[i].isalpha()):
            ans=[k+j for k in ans for j in (S[i],S[i].swapcase())]
        else:
            ans=[k+S[i] for k in ans]
    return ans

    
    '''Bitmasking 
    n=len(S)
    ans=[]
    G=set()
    for i in range(pow(2,n)):
        path=""
        for j in range(n):
            if (i&(1<<j)):
                path=path+S[j].swapcase()
            else:
                path=path+S[j]
        if path not in G:
            ans.append(path)
            G.add(path)
    return ans'''

print(solve("a1b2"))
