'''

Given a binary tree, find its maximum depth.
给定二叉树，找到它的最大深度。
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

思路： 由于树是一种递归的数据结构，所以一般用递归做
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,root):
        if root is None :
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            return max(l, r) + 1

if __name__=='__main__':
    s = Solution()
    root = TreeNode(3)
    l = TreeNode(9)
    r = TreeNode(20)
    l1 = TreeNode(15)
    r1 = TreeNode(7)
    root.left = l
    root.right = r
    r.left = l1
    r.right = r1
    result = s.maxDepth(root)
    print (result)

