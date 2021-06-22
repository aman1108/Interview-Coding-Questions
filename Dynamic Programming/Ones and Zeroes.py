def solve(strs,m,n):
    DP=[[-1 for i in range(m+1)] for j in range(n+1)]
    DP[0][0]=0

    ans=0
    for val in strs:
        zero=val.count("0")
        one=len(val)-zero

        for i in range(n-one,-1,-1):
            for j in range(m-zero,-1,-1):
                if (DP[i][j]!=-1):
                    DP[i+one][j+zero]=max(DP[i+one][j+zero],1+DP[i][j])
                    ans=max(ans,DP[i+one][j+zero])
    return ans


print(solve(["10","0001","111001","1","0"],5,3))
print(solve(["10","0001","111001","1","0"],1,1))

print(solve(["10000","000011","1110001","1","11110","1110101","100","1110"],9,10))
