# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        
        self.nodes = []
        head = point = ListNode(0)  # 创建一个首节点，point用于扫描
        
        for list in lists:          # 扫描所有值
            while list:
                self.nodes.append(list.val)
                list = list.next
                
        for val in sorted(self.nodes):
            point.next = ListNode(val)
            point = point.next
        return head.next
            
