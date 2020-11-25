def solve(A):
    s=""
    for i in A:
        s=s+str(i)

    s=int(s)+1
    s=str(s)
    B=[]
    for i in s:
        B.append(int(i))

    return B

print(solve([1,2,3]))
    
        
