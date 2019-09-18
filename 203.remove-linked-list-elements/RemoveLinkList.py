'''
删除链表指定值
https://leetcode.com/problems/remove-linked-list-elements/description/
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
    思路： 链表的基本操作，移除某个特定的值，
            通常设置一个 head指定链表的头，后面好操作
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def removeLinkList(self,head,val):
        pre = ListNode(0)
        pre.next = head
        cur = pre
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return pre.next

if __name__ == "__main__":
    head = ListNode(0)
    first = ListNode(1)
    second = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    head.next = first
    first.next = second
    second.next = three
    three.next = four

    s = Solution()
    s.removeLinkList(first,3)
    cur = head
    while cur.next:
        print(cur.val)
        cur = cur.next
    print (cur.val)

