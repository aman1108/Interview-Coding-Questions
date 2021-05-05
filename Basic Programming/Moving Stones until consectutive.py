def solve(a,b,c):
    a,b,c=sorted([a,b,c])
    cnt=min((b-a),(c-a),(c-b))
    if (cnt<3):    
        return[min(1,c-a-2),c-a-2]
    return [min(2,c-a-2),c-a-2]

print(solve(3,5,1))
