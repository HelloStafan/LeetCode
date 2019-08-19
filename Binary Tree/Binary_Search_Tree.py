# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.counter = 0
        self.res = None

    def kthSmallest(self, root, k):
       
        # 定义 中序遍历 函数
        def inorder(root, k):         
             # 先递归 标记左子树
            if root.left:
                inorder(root.left, k)
        
            self.counter += 1  # 标记

            if self.counter == k:  # 判断是不是要的那个数  
                self.res = root.val
           
            # 最后递归 标记右子树
            if root.right:
                inorder(root.right, k)
                
        inorder(root, k)
        return self.res
        
