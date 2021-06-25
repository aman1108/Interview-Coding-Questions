from collections import defaultdict
def solve(words):
    words=list(set(words))
    n=len(words)
    G=defaultdict(list)

    for val in words:
        val=val[::-1]
        flag=0
        cur=G
        for a in val:
            if a in cur and flag==0:
                cur=cur[a]

            else:
                cur[a]=defaultdict(list)
                cur=cur[a]
                flag=1

    ans=0
    for val in words:
        val=val[::-1]
        flag=0
        cur=G
        for a in val:
            if a in cur and flag==0:
                cur=cur[a]
        
        if(len(cur)==0):
            ans=ans+len(val)+1
    return ans

print(solve(["time","me","bell"]))
    
    
