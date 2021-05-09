# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def solve(root,val):
            root.val=val[0]
            left=[]
            right=[]
            for i in range(1,len(val)):
                if (val[0]<val[i]):
                    right.append(val[i])
                else:
                    left.append(val[i])
            if (len(left)>0):
                lnode=TreeNode()
                root.left=lnode
                solve(lnode,left)
            if (len(right)>0):
                rnode=TreeNode()
                root.right=rnode
                solve(rnode,right)
        
        root=TreeNode()
        temp=root
        solve(temp,preorder)
        return root
        
        
