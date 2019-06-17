

'''
无重复字符的最长子串
给定一个字符串，找出不含重复字符的最长字符子串
思路：字典记录值相对应的位置
'''

class Solution:
    def LongSubstring(s):
        '''
        :param target:string
        :return: int
        '''
        st = {}     #记录每个值得位置
        i, ans = 0, 0   # i起始位置  ans 最大长度

        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans
    def lengthOfLongestSubstring(s):
        '''
        :param s: str
        :return: int
        '''
        l = 0   #最大长度
        start = 0   #左边位置
        dic = {}
        for i in range(len(s)):
            cur = s[i]  #当前值
            if cur not in dic.keys():
                dic[cur] = i    #不存在，记录位置
            else:
                if dic[cur] + 1 > start:
                    start = dic[cur] + 1    #存在，把起始位置移到重复字符的位置
                dic[cur] = i
            if i - start + 1 > l:
                l = i -start + 1
        return l

if __name__ == "__main__":
    str= "qwertyq"
    print (Solution.LongSubstring(str))
    s = Solution()
    print (Solution.lengthOfLongestSubstring(str))









