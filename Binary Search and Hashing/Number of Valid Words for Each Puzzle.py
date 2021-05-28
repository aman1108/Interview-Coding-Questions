from collections import defaultdict

def solve(words,puzzles):
    n=len(words)
    m=len(puzzles)

    G=[defaultdict(lambda:0) for i in range(26)]
    for val in words:
        bitmask=0
        for i in val:
            cnt=ord(i)-97
            bitmask=bitmask|(1<<cnt)

        s=set(val)
        for j in s:
            v=ord(j)-97
            G[v][bitmask]+=1
        
    ans=[0]*m
    for j in range(m):
        val=puzzles[j]
        bitmask=0
        for i in val:
            cnt=ord(i)-97
            bitmask=bitmask|(1<<cnt)

        v=ord(val[0])-97
        original=bitmask
        
        while(bitmask!=0):
            ans[j]=ans[j]+G[v][bitmask]
            bitmask=(bitmask-1)&original
            
    return ans
        
        

print(solve(["apple","pleas","please"],["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]))
print(solve(["aaaa","asas","able","ability","actt","actor","access"],["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
