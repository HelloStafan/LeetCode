class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = nums[0];
        sum = 0;  # sum为数组的累和
        
        for num in nums:  
            '''
            遍历数组：
            对于每一个元素num，若sum(该元素之间元素的累和)<0，
            则抛弃之前的元素，即sum = num；
            否则不抛弃之前的元素，继续把当前元素加上；

            '''        
            if(sum > 0):
                sum += num;
            else:
                sum = num;
                
            ans = max(ans, sum);  # 更新ans
        return ans;
    
