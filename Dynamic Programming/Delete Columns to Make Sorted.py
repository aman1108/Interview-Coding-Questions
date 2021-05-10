def solve(strs):
    n=len(strs)
    w=len(strs[0])
    DP=[1 for i in range(w)]

    for i in range(w):
        for j in range(i):
            cnt=0
            for k in range(n):
                if (strs[k][i]<strs[k][j]):
                    break
                cnt=cnt+1
            if (cnt==n):
                DP[i]=max(DP[i],1+DP[j])
                
    print(DP)
    return w-max(DP)

print(solve(["babca","bbazb"]))
