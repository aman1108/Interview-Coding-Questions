'''Leetcode submisision:
class Solution:
    ans=[]
    def solve(self,A,l,r):
        if (l==r):
            B=[i for i in A]
            self.ans.append(B)
        for i in range(l,r+1):
            A[l],A[i]=A[i],A[l]
            self.solve(A,l+1,r)
            A[l],A[i]=A[i],A[l]


    def permute(self, nums: List[int]) -> List[List[int]]:
            n=len(nums)
            self.ans=[]
            self.solve(nums,0,n-1)
            return self.ans

        
        '''

def solve(A,l,r,ans):
    if (l==r):
        B=[i for i in A]
        ans.append(B)
    for i in range(l,r+1):
        A[l],A[i]=A[i],A[l]
        solve(A,l+1,r,ans)
        A[l],A[i]=A[i],A[l]
        
    
def permute(A):
    n=len(A)
    ans=[]
    solve(A,0,n-1,ans)
    print(ans)

permute([1,2,3])
    
