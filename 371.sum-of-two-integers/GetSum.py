'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
计算两个整数a和b的总和，
但不允许使用+和-运算符。
范例1： 输入：a = 1，b = 2 输出3 范例2： 输入：a = -2，b = 3 输出1
Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1

思路： 异或运算，相同为1，不同为0可以表示不带进位的加减
        与运算，全部为1则为1，其他都为0， 所以可以把与算法的结果再 向左移动，表示进位
        递归：到其中一个为0就返回结果
        js
var getSum = function(a, b) {
    if (a === 0) return b;

    if (b === 0) return a;

    return getSum(a ^ b, (a & b) << 1);
};
'''

class Solution:
    def getSum(self,a,b):
        if a == 0:
            return b
        if b == 0:
            return a
        return self.getSum(a^b,(a&b)<<1)


if __name__=="__main__":
    s = Solution()
    a = -1
    b = 1
    print (s.getSum(a,b))