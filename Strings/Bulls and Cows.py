from collections import defaultdict
def solve(secret,guess):
    gt=""
    G=defaultdict(lambda:0)
    n=len(guess)
    x,y=0,0
    for i in range(n):
        
        if (secret[i]==guess[i]):
            x=x+1

        else:
            G[secret[i]]+=1
            gt=gt+guess[i]
            
    for val in gt:
        if G[val]>0:
            G[val]=G[val]-1
            y=y+1

    return str(x)+"A"+str(y)+"B"
            
print(solve("1807","7810"))
