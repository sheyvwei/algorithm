'''
172.
https://leetcode.com/problems/factorial-trailing-zeroes/description/
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

思路: 看规律，https://github.com/azl397985856/leetcode/blob/master/problems/172.factorial-trailing-zeroes.md

'''

class Solution:
    def trailingZeros(self, n):
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count

if __name__ == "__main__":
    n = 30
    s = Solution()
    result = s.trailingZeros(n)
    print (result)