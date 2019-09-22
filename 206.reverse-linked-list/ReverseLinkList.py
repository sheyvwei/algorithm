'''
206.
Reverse a singly linked list.
反转链表
Example:

Input: 1->2->3->4->5->NULL Output: 5->4->3->2->1->NULL Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

思路：  设置一个前一个节点 pre
        令 cur 为当前head cur = head
        循环链表，两个值的next之间进行交换
        交换next的时候，从后面开始交换就不会出错：
        先记录next = cur.next
        赋值cur.next  cur.next = pre
        再赋值当前的cur给pre   pre = cur
        最后 cur向前， cur = next


'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def reverseList(self,head):
        if not head:
            return None
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

if __name__=="__main__":
    head = ListNode(1)
    first = ListNode(2)
    second = ListNode(3)
    three = ListNode(4)
    four = ListNode(5)
    head.next = first
    first.next = second
    second.next = three
    three.next = four
    s = Solution()
    result = s.reverseList(head)

    cur = result
    while cur:
        print (cur.val)
        cur = cur.next
