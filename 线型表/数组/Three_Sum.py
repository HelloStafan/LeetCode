class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()  # 排序，关键点
        res, k = [], 0
        
        # 遍历数组，固定k；i为左指针，在k右一位，j为右指针，在数组末尾
        for k in range(len(nums) - 2):
            
            # 特殊情况处理
            if nums[k] > 0: break 
            if k > 0 and nums[k] == nums[k - 1]: continue
                
            i, j = k + 1, len(nums) - 1
            
            while i < j: 
                sum = nums[k] + nums[i] + nums[j]
                if sum < 0:  # <0，过小，i右移 
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif sum > 0:  # >0，过大，j左移
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:  # =0，记录
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res
        
