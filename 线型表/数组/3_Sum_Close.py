
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()  # 排序，关键点
        close =  1000
        min_sum = 1000
        k = 0

        for k in range(len(nums)-2):
            i, j = k+1 , len(nums)-1  #　左右指针

            while i < j: 
                sum = nums[k] + nums[i] + nums[j]

                if abs(sum-target) < close:  # 比较最小值
                    close = abs(sum-target)
                    min_sum = sum

                if sum < target:
                    i += 1
                elif sum > target:
                    j -= 1
                else:
                    return min_sum
                
                # while i < j and nums[i] == nums[i - 1]: i += 1
                # while i < j and nums[j] == nums[j + 1]: j -= 1
        return min_sum

    
# 测试
nums = [1, 1, 1, 0]
solution = Solution()
print( solution.threeSumClosest(nums, 1))
