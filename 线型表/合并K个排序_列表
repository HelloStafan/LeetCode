class Solution:
    def mergeKLists(self, *L1) :
        lists = [*L1]  # 待合并集

        n = len(lists)-1    # 总比较次数n
        for _ in range(n):  
            a,b = lists[0],lists[1] 
            lists.pop(0)
            lists.pop(0)    # 赋值好后,删除

            c = []
            i,j = 0,0
            while True:
                if i==len(a):
                    c.extend(b[j:])
                    lists.append(c)   # 将 a,b的合并后的c加入待合并集
                    break             # 1.跳出while循环,否则MemoryError
                elif j==len(b):
                    c.extend(a[i:])
                    lists.append(c)   # 将 a,b的合并后的c加入待合并集
                    break
                else:
                    if a[i]<b[j]:
                        c.append(a[i])
                        i=i+1
                    else:
                        c.append(b[j])
                        j=j+1
        return lists[0]
