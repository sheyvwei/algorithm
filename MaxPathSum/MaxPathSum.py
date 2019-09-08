'''
Given a non-empty binary tree, find the maximum path sum.
给定非空二叉树，找到最大路径总和。 对于此问题，路径定义为沿着父子连接从树中的某个起始节点到任何节点的任何节点序列。该路径必须至少包含一个节点，并且不需要通过根节点。
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

思路：
    树一般用递归算法
    递归  max(this.val, this.val+lefMax,this.val + rightMax)

'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    maxSum = float('-inf')
    def maxPathSum(self,root):
        self.maxPathSumHelper(root)
        return self.maxSum
    def maxPathSumHelper(self,node):
        if node is None:
            return 0
        leftMax = self.maxPathSumHelper(node.left)
        rightMax = self.maxPathSumHelper(node.right)
        self.maxSum = max(self.maxSum,max(node.val+leftMax + rightMax, max(node.val,max(node.val+leftMax,node.val+rightMax))))
        return max(node.val, max(node.val + leftMax, node.val+rightMax))

if __name__ == "__main__":
    root = TreeNode(-10)
    l = TreeNode(9)
    r = TreeNode(20)
    l2 = TreeNode(15)
    r2 = TreeNode(7)
    s = Solution()
    root.left = l
    root.right = r
    root.right.left = l2
    root.right.right = r2
    result = s.maxPathSum(root)
    print (result)