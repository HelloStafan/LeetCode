
# 常规方法
# 2^num = n
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and 2**int(math.log2(n)) == n
    
    
# 将n转化为二进制，查看其特点  
# n的最高位为1，其余位为0，形如 1000，则n-1则为 0111
class Solution: 
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&n-1 == 0
