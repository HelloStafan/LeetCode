class Solution(object):
            
    def sortList(self, head):

        if head is None or head.next is None:
            return head

        left = head               # 头节点为左头
        mid = self.get_mid(head)  # 中间数
        right = mid.next          # 中间数的下一个为右头

        mid.next = None           # 分裂

        return self.merge(self.sortList(left), self.sortList(right))

    # 合并 
    def merge(self, l1, l2):

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2

    # 取中间数
    def get_mid(self, head):
        
        if head is None:
            return head

        slow = fast = head  # 快慢指针
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return  slow
