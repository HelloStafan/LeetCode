'''
    在一个整数数组中,找出众数 (个数>=n/2)
    1.普通方法
    2.投票算法
    3.哈希表
    4.位运算

'''
# 普通方法 超时
class Solution:
    def majorityElement(self, nums) :

        max_ = len(nums)/2
        major = 0
        for num in nums:
            major = num if nums.count(num) > max_ else major
        return major

# Boyer-Moore 投票算法
class Solution:
    def majorityElement(self, nums) :

        count = 0  # 投票计数器
        for num in nums:
            if count == 0:
                major = num
            if num == major:
                count += 1
            else:
                count -= 1
        return major


# 测试  
solution = Solution()
print(solution.majorityElement([3,2,3]))

