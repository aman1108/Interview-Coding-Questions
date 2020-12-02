def solve(A,B):
    n=len(A)
    ans=0
    i=0
    while(i<n):
        #print(i)
        flag=0
        j=min(i+B-1,n-1)
        while(j>=max(i-B+1,0)):
            if (A[j]==1):
                flag=1
                ans=ans+1
                break
            j=j-1
                
        if(flag==0):
            return -1
        i=j+B
        
    return ans

print(solve([ 0, 0, 1, 1, 1, 0, 0, 1],3))
 
print(solve([ 0, 0, 0,1,0],3))

print(solve([1,1,1,1],3))

print(solve([ 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0 ],12))
