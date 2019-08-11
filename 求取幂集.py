# 求集合的幂集
'''
    可知
        []的幂集 = []
        [1]的幂集 = [],[1]
        [1,2]的幂集 = [],[1],  [2],[1,2]
        [1,2,3]的幂集 = [],[1],[2],[1,2],  [3],[1,3],[2,3],[1,2,3]

    后一个幂集 = 前一个幂集本身 + 前一个幂集各项各自加上列表多出的数    

'''      
class Solution:
    def subsets(self, nums):
        lists = [[]]  # 幂集
        
        for num in nums:  
            lists +=  [ [num] + l  for l in lists]
        return lists

a = Solution()
print(a.subsets([1,2]))
