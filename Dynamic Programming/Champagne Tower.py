def solve(poured,query_row,query_glass):
    x=poured
    v=min(1,x)
    DP=[[v,x-v]]
    
    for i in range(2,query_row+2):
        DP1=[]
        for j in range(i):
            if (j==0):
                v=DP[j][1]/2
                mv=min(1,v)
                DP1.append([mv,v-mv])
            elif (j==(i-1)):
                v=DP[j-1][1]/2
                mv=min(1,v)
                DP1.append([mv,v-mv])

            else:
                v=(DP[j][1]/2)+(DP[j-1][1]/2)
                mv=min(1,v)
                DP1.append([mv,v-mv])
        #print(DP1)
        DP=DP1.copy()

    #print(DP)
    val=DP[query_glass][0]
    return val


#print(solve(100000009,33,17))
#print(solve(7,3,3))
print(solve(0,0,0))
