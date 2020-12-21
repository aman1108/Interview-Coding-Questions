#problem link: https://www.interviewbit.com/problems/woodcutting-made-easy/
def solve(A,B):
    n=len(A)
    beg=min(A)
    end=max(A)
    ans=beg
    while(beg<=end):
        #print(beg,end)
        mid=(beg+end)//2
        cnt=0
        for i in range(n):
            cnt=cnt+max(A[i]-mid,0)

        if (cnt>=B):
            beg=mid+1
            ans=max(ans,mid)
        else:
            end=mid-1

    return ans

print(solve([4,42,40,26,46],20))
