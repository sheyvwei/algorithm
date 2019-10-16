'''
Given a linked list, remove the n-th node from the end of list and return its head.
给定一个链表，从列表末尾删除第n个节点并返回其头。
Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5. Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

思路： 快慢指针
'''
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head, n):
        dummyHead = ListNode(0)
        dummyHead.next = head
        fast = slow = dummyHead
        i = 0
        while(fast.next):
            if i >= n:
                slow = slow.next
            fast = fast.next
            i += 1
        slow.next = slow.next.next
        return dummyHead.next
if __name__ == "__main__":
    s = Solution()
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    result = s.removeNthFromEnd(one,2)
    while(result):
        print (result.val)
        result = result.next