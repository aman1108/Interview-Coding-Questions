# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans=1
        def solve(node,val):
            nonlocal ans
            tnode=[]
            tval=[]
            for i in range(len(val)):
                a=node[i]
                v=val[i]
                if (a.left):
                    tnode.append(a.left)
                    tval.append(2*v)
                if (a.right):
                    tnode.append(a.right)
                    tval.append((2*v)+1)
            if (len(tval)):
                #print(tval)
                ans=max(ans,tval[-1]-tval[0]+1)
                solve(tnode,tval)
        solve([root],[1])
        return ans
        
