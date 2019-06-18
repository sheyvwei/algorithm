

'''
回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数
121  true
-121 false
'''

class Solution:
    def Palindrome(self,s):
        '''
        :param s: string
        :return: bool
        '''
        str_s = str(s)    # 整数转字符串
        for i in range(0, int(len(str_s)/2)):
            if str_s[i] != str_s[-i-1]:
                return False
        return True

if __name__ == "__main__":
    s = 121
    solution = Solution()
    print (solution.Palindrome(s))
