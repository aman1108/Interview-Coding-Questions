# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        def dfs(node,mv):
            nonlocal ans
            if node:
                if (node.val>=mv):
                    mv=node.val
                    ans=ans+1
                
                dfs(node.left,mv)
                dfs(node.right,mv)
        dfs(root,-1*float("inf"))
        return ans
