# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=root
        def dfs(node):
            nonlocal ans
            if node:
                x=dfs(node.left)+dfs(node.right)
                if (node==p):
                    x=x+1
                elif(node==q):
                    x=x+1

                #print(node.val,x)
                if (x==2):
                    ans=node
                    return 0
                return x
            return 0
        
        dfs(root)
        return ans
        
        
        
        
        
                
