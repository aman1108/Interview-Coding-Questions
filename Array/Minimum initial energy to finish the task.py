def solve(tasks):
    n=len(tasks)
    tasks.sort(key=lambda x: x[0]-x[1])
    ans=0
    eng=0
    for i in range(n):
        ans=ans+max(max(tasks[i][0],tasks[i][1])-eng,0)
        eng=max(tasks[i][1]-tasks[i][0],0)+max(eng-max(tasks[i][0],tasks[i][1]),0)
        #print(ans,eng)
    return ans

print(solve([[1,1],[1,3],[1,3]]))
        
#print(solve([[1,3],[2,4],[10,11],[10,12],[8,9]]))
#print(solve([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]))
