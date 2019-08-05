class Min_Stack(object):  

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []  # 数据栈
        self.min_list = []  # 最小值栈
    
    def push(self, element):
        self.list.append(element)
        if not self.min_list or element <= self.min_list[-1]:  
        	self.min_list.append(element)
    
    def pop(self):       
            if self.list[-1] == self.min_list[-1]:
            	self.min_list.pop()
            self.list.pop()
                
    def top(self):
            return self.list[-1]
        
    def getMin(self):
            return self.min_list[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = Min_Stack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
