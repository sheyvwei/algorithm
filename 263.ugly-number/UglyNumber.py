'''
263.
https://leetcode.com/problems/ugly-number/description/
判断你一个数是否为 丑数： 正数，并且，因子只包括2，3，5

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1]
思路： 只要一直除以 2，3,5，当最后结果为1时，便是丑数
'''


class Solution:
    def uglyNumber(self,num):
        if num <= 0:
            return False
        while num%2==0:
            num = num /2
        while num%3== 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        return num == 1

if __name__ == "__main__":
    s = Solution()
    num = 6
    result = s.uglyNumber(num)
    print (result)

