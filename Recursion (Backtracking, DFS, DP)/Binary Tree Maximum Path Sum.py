# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ans=-(10**9)
        def solve(node):
            nonlocal ans
            if (node):
                x=solve(node.left)
                y=solve(node.right)
                #print(node.val,x,y)
                ans=max(ans,node.val+max(x,0)+max(y,0))
                return node.val+max(x,y,0)
            return 0
        solve(root)
        return ans
        
