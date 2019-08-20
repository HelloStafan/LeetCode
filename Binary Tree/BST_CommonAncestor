# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 根据二叉搜索树(BST)的定义 ，某根节点的右子树>=根节点 某根节点的左子树<=根节点
# 因此，当 p，q 最先开始分叉的那个节点便是 最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        root_val = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val > root_val and q_val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < root_val and q_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return root
    
