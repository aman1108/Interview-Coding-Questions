def solve(emails):
    n=len(emails)
    G={}
    cnt=0

    for i in range(n):
        s=emails[i]
        t=""
        flag=0
        for j in s:
            if (flag==2 and j!="@"):
                continue
            
            if (j=="." and flag==0):
                continue

            if (j=="+" and flag==0):
                flag=2
                continue

            if (j=="@"):
                t=t+j
                flag=1
                
            else:
                t=t+j
                
        #print(s,t)
        if t not in G:
            G[t]=1
            cnt=cnt+1

    return cnt

#print(solve(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(solve(["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]))
