def numberOfMatches(n):
    if (n==1):
        return 0
    elif (n%2==0):
        return (n//2)+numberOfMatches(n//2)     #write self.numberOfMatches(n//2) on leetcode
    else:
        return ((n-1)//2)+numberOfMatches(1+((n-1)//2))

print(numberOfMatches(14))
    
