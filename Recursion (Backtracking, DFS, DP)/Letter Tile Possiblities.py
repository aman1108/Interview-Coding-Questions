def solve(tiles):
    n=len(tiles)
    tiles=list(tiles)
    ans=set()
    def fun(tiles,path):
        for i in range(n):
            if (tiles[i]!=-1):
                temp=path+tiles[i]
                if temp not in ans:
                    ans.add(temp)
                    tiles[i]=-1
                    fun(tiles,temp)
                    tiles[i]=temp[-1]
    
    fun(tiles,"")
    return len(ans)

print(solve("AAB"))
print(solve("AAABBC"))
print(solve("V"))
