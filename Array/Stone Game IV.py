def solve(n):
    pref=[0 for i in range(n+1)]

    for i in range(n):
        if (pref[i]==0):
            j=1
            while ((i+(j*j))<=n):
                pref[(i+(j*j))]=1
                j=j+1

    return pref[n]

print(solve(35))
                
