# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root ==q:
            return root
        
        else:
            left = self.lowestCommonAncestor(root.left, p, q)   # 左子树是否 存在 p，q
            right = self.lowestCommonAncestor(root.right, p, q) # 右子树是否 存在 p，q
        
        if right and left:
            return root
        
        elif left :
            return left
        elif right:
            return right
        else:
            return None
