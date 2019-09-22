'''
226.反转二叉树
* Example:
 *
 * Input:
 *
 *
 * ⁠    4
 * ⁠  /   \
 * ⁠ 2     7
 * ⁠/ \   / \
 * 1   3 6   9
 *
 * Output:
 *
 *
 * ⁠    4
 * ⁠  /   \
 * ⁠ 7     2
 * ⁠/ \   / \
 * 9   6 3   1

 思路： 递归或者栈
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertBinaryTree(self,root):
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return
    def invertTree2(self,root):
        if not root:
            return None
        root.left, root.right = self.invertTree2(root.right),self.invertTree2(root.left)
        return root