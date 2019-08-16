# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 递归的思想 
# 求取某节点的最大深度，就是求其两个子节点的最大深度，依次类推
class Solution:
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            D_left = self.maxDepth(root.left)
            D_right = self.maxDepth(root.right)
            return max(D_left, D_right)+1
        
