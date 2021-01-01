def solve(A,B):
    l=A
    r=B
    ans=[]
    if (A==0):
        ans.append(0)
    for i in range(1,10):
        Q=[i]
        while(len(Q)!=0):
            a=Q.pop()
            if (a>=l and a<=r):
                ans.append(a)

            if (a>r):
                continue

            else:
                ld=a%10
                if (ld==0):
                    a=(a*10)+1
                    Q.append(a)

                elif (ld==9):
                    a=(a*10)+8
                    Q.append(a)

                else:
                    Q.append((a*10)+(ld-1))
                    Q.append((a*10)+(ld+1))
    ans.sort()
    return ans

print(solve(1,30))
