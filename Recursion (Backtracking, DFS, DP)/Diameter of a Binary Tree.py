# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans=0
        def solve(node):
            nonlocal ans
            if node:
                x=solve(node.left)
                y=solve(node.right)
                ans=max(ans,x+y)
                #print(node.val,x,y)
                return max(x+1,y+1)
            else:
                return 0
        solve(root)
        return ans
        
