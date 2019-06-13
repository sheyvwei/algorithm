
'''
两个链表的数字相加
(2 -> 4 -> 3) + (5 -> 6 -> 4)
 7 -> 0 -> 8
 243 + 564 = 807.
 pHead=pNode     pNode 移位 pNode    pNode
 0 》》》 7 》》》 0 》》》 8
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def TwoSumForList(self, l1, l2):
        pNode = ListNode(0) #用来移位
        pHead = pNode   #当做链表头
        flag = 0
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 or l2:
            sum = 0  #每项结果
            if l1:
                sum = l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next
            sum = sum + flag
            flag = ((sum +flag) // 10)   #  是否有进位//取整数
            pNode.next = ListNode(sum % 10)
            pNode = pNode.next  #移位
        if flag:
            pNode.next = ListNode(1)  #最后如果还有进位加1

        return pHead.next

if __name__ == '__main__':
    #print (100 //10)
    t1 = ListNode(3)
    t2 = ListNode(4)
    t2.next = t1
    t3 = ListNode(2)
    t3.next = t2

    k1 = ListNode(4)
    k2 = ListNode(6)
    k2.next = k1
    k3 = ListNode(5)
    k3.next = k2
    re = Solution()
    # result = t3     ##test
    result = re.TwoSumForList(t3,k3)
    while (result != None):
        print(result.val)
        result = result.next