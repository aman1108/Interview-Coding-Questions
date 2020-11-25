def solve(A,B):
            n=len(A)
            ans=0
            x,y=A[0],B[0]
            for i in range(1,n):
                ans=ans+max(abs(x-A[i]),abs(y-B[i]))
                x,y=A[i],B[i]
            return ans
        
A = [0, 1, 1]
B = [0, 1, 2]
print(solve(A,B)) 
