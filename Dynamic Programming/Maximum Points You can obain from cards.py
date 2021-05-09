def solve(cardPoints,k):
    n=len(cardPoints)
    k=n-k
    ans=sum(cardPoints)
    s=0
    temp=ans
    for i in range(k):
        s=s+cardPoints[i]
    temp=min(s,temp)
    for i in range(k,n):
        s=s+cardPoints[i]-cardPoints[i-k]
        temp=min(s,temp)
    return ans-temp

        
print(solve([11,49,100,20,86,29,72],4))
