#https://www.interviewbit.com/problems/equal/
def solve(A):
        n=len(A)
        G={}
        for i in range(n):
            for j in range(i+1,n):
                try:
                    G[A[i]+A[j]].append([i,j])
                except:
                    G[A[i]+A[j]]=[[i,j]]
                    
        flag=0
        ans=[float("inf"),float("inf"),float("inf"),float("inf")]
        for i in G:
            if (len(G[i])>1):
                G[i].sort()
                flag1=0
                for j in range(len(G[i])):
                    for k1 in range(j,len(G[i])):
                        x,y,a,b=G[i][j][0],G[i][j][1],G[i][k1][0],G[i][k1][1]
                        C=[x,y,a,b]
                        C.sort()
                        vf=0
                        for k in range(3):
                            if (C[k]==C[k+1]):
                                vf=1
                                break
                        if (vf==0):
                            flag=1
                            flag1=1
                            ans=min(ans,[x,y,a,b])
                            break
                    if(flag1==1):
                        break
        if(flag==0):
            return ([]) 
            
        return ans
print(solve([3,4,7,1,2,9,8]))
#print(solve([0,0,1,0,2,1]))
