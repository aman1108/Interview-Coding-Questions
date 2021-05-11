def solve(arr):
    n=len(arr)
    G=set()
    S=set()
    
    for i in range(n):
        S.add(arr[i])
        temp=set()
        for v in S:
            G.add(arr[i]|v)
            temp.add(arr[i]|v)

        S=temp
    #print(G)
    return len(G)

print(solve([1,2,4]))
print(solve([13,4,2]))
