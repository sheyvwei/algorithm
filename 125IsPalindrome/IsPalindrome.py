'''
125 给定一个字符串，确定它是否是回文，只考虑字母数字字符并忽略大小写。 注意：出于此问题的目的，我们将空字符串定义为有效的回文
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
思路： 回文数一般用头尾双指针
'''

class Solution:
    def isPalindrome(self, s):
        start = 0
        last = len(s) - 1
        while start < last:
            if not s[start].isalnum():
                start +=1
                continue
            if not s[last].isalnum():
                last -=1
                continue
            if s[start].lower() == s[last].lower():
                start += 1
                last -= 1
                continue
            else:
                return False
        return True

if __name__=="__main__":
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.isPalindrome(s)
    print (result)