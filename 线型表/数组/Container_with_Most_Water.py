class Solution:
    def maxArea(self, height):
        
        '''
        双指针：left right
        '''
        maxarea = 0
        l = 1
        r = len(height)
    
        while l<r:
            left = height[l-1]  # 初始化在首
            right = height[r-1]  # 初始化在末尾
            
            area = min(left, right) * (r-l)  # 计算当前面积
            maxarea = max(maxarea, area)  # 更新面积最大值 
            
            if left > right:
                r -= 1
            else:
                l += 1
                
        return maxarea
