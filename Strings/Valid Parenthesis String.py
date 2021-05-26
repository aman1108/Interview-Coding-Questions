def solve(s):
    n=len(s)
    low,high=0,0

    for i in range(n):
        if (s[i]=="("):
            low=low+1
            high=high+1

        elif(s[i]==")"):
            if(high==0):
                return 0
            low=max(low-1,0)
            high=high-1

        else:
            low=max(low-1,0)
            high=high+1

    if(low==0):
        return 1
    return 0

print(solve("*)(()))"))
