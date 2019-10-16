'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
定字符串s，找到s中最长的回文子字符串。您可以假设s的最大长度为1000
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

思路: 动态规划
python初始化列表 1; 一维列表： L = [5] * 5
                2: 二维列表： L = [ [0] * 5 for i in range(5)]
for循环从n到0进行: def foo(n):
                    for i in range(n, 0, -1):
                    print(i)
'''




class Solution:
    def longestPalindrome(self,s):
        if not s:
            return ''
        str_length = len(s)
        res = s[:1]
        dp = [[0 for i in range(str_length)] for i in range(str_length)]
        for i in range(str_length-1, -1, -1):
            for j in range(i,str_length, 1):
                if j - i == 0:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
        return res

if __name__ == "__main__":
    s = Solution()
    str = "babad"
    str = "bb"
    result = s.longestPalindrome(str)
    print (result)



