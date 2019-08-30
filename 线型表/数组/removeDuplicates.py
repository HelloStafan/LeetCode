
# 注意 是排序数组
class Solution:
    def removeDuplicates(self, nums):
        
        count = 0 
        tem = None
        
        for num in nums:  # 遍历，时间复杂度O(n)
            if num != tem:
                nums[count] = num
                tem = num
                count += 1
                
        return count  # 注意 是count
