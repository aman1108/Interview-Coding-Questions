def solve(s):
    n=len(s)
    for i in range(n//2):
        s[i],s[n-i-1]=s[n-i-1],s[i]

s=["h","e","l","l","o"]
s=["H","a","n","n","a","h"]
solve(s)
print(s)
