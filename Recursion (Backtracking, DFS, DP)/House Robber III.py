# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def fun(node):
            if (node):
                x1,y1=fun(node.left)
                x2,y2=fun(node.right)
                #print(node.val,x1,x2,y1,y2)
                return max(y1+y2+node.val,x1+x2),x1+x2
            return 0,0
        return max(fun(root))
        
