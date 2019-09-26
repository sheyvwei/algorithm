'''
You are given a binary tree in which each node contains an integer value.
您将获得一个二叉树，其中每个节点都包含一个整数值。 查找总计为给定值的路径数。
 该路径无需在根或叶处开始或结束，但必须向下（仅从父节点移动到子节点）。
  该树的节点数不超过1,000，其值在-1,000,000至1,000,000范围内
Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def helper(self,root, sum):
        if not root:
            return 0
        l = self.helper(root.left, sum - root.val)
        r = self.helper(root.right, sum-root.val)
        return l + r + (1 if root.val == sum else 0)
    def pathSum(self,root,sum):
        if not root:
            return 0
        rt = self.helper(root, sum)
        l = self.pathSum(root.left, sum)
        r = self.pathSum(root.right,sum)
        return rt + l + r
    def pathSumByTest(self,root, sum):
        if not root:
            return 0
        l = self.pathSumByTest(root.left, sum - root.val)
        r = self.pathSumByTest(root.right, sum-root.val)
        return l + r + (1 if root.val == sum else 0)

if __name__=="__main__":
    a = 8
    # a = 1 if b>c else 0    等价于  a = b> c ? 1: 0
    1 if a == 7 else 0
    print (1 if a == 8 else 0)





























