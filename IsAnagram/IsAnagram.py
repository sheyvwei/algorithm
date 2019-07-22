
'''
题目：https://leetcode-cn.com/problems/valid-anagram/
描述：给定两个字符串给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词
    true:  s = "anagram", t = "nagaram"
    false: s = "rat", t = "car"
思路：
'''

class Solution:
    def isAnagram(self,s,t):
        """
        :param s:str
        :param t:str
        :return:bool
        """
        return sorted(s) == sorted(t)


if  __name__ == '__main__':
    s = 'anagram'
    t = 'nagaram'
    solution = Solution()
    print (solution.isAnagram(s,t))