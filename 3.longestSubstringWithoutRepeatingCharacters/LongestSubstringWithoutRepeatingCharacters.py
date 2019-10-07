
'''

Given a string, find the length of the longest substring without repeating characters.
给定一个字符串，找到最长子字符串的长度而不重复字符。
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and n

    思路： 字典记录位置， 两个相同字母之间的距离就是无重复字符的长度

'''

class Solution:
    def lengthOfLongestSubstring(self,s):
        map = {}
        left = 0
        maxLeng = 0
        for i in range(len(s)):
            if s[i] in map:
                #更新左边
                left = max(map[s[i]], left)
            #每次都要计算下面的式子，计算最长的值以及如果重复也直接赋值到map更新最新值
            maxLeng = max(maxLeng, i - left + 1)
            map[s[i]] = i + 1
        return maxLeng

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        left, maxLeng = 0, 0
        for i in range(len(s)):
            if s[i] in st:
                left = max(st[s[i]], left)
            maxLeng = max(maxLeng, i - left + 1)
            st[s[i]] = i + 1
        return maxLeng

if __name__ == "__main__":
    s = Solution()
    # str = "pwwkew"
    # str = "abcabcbb"
    # str = "dvdf"
    str = "tmmzuxt"
    result = s.lengthOfLongestSubstring(str)
    # result = s.lengthOfLongestSubstring2(str)

    print (result)



