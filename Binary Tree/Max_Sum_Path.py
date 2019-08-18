# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
     
    
    def maxPathSum(self, root: TreeNode) -> int:
        res = float('-inf')
        
        def max_Sum(node):  # 参数为一个节点，返回以该节点为终点的最大路径和
            
            nonlocal res
            if not node:
                return 0

            left_path = max(max_Sum(node.left), 0)    # 与0比较，只加正数
            right_path = max(max_Sum(node.right), 0)  # 与0比较，只加正数

            res = max(left_path+right_path+node.val, res)

            return max(left_path, right_path)+node.val 
        
        max_Sum(root)
        return res
