# 在一个整数数组中,找出不同的数

class Solution:
    def singleNumber(self, nums):

        # 利用字典来存储不同值的不同情况
        dict_ = {}

        for num in nums:
            if num in dict_ :
                dict_[num] = 2
            else:
                dict_[num] = 1

        # 键值转换
        dict_ = {v: k for k, v in dict_.items() if v == 1}
        
        # 提取键
        return [k for k in dict_.values()][0]

# 测试
solution = Solution()
# print( solution.singleNumber([1,1,2,2,3]) )


# 别的方法
class Solution:
    def singleNumber(self, nums):

        # 1.利用集合set去重
        #return sum(set(nums))*2-sum(nums)
        
        # 2. 异或操作
        res=0
        #  原理：将数组内的所有数外加0, ^相连
        #         1.两数字相同时,^得0
        #         2.任何数 ^ 0 = 任何数 
        for num in nums:
            res ^= num
            print(res)
        return res
