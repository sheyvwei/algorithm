'''
https://leetcode.com/problems/reverse-bits/description/
反转2进制的32位无符号数字，
Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.
思路： n&1 可以取最后一个数字是什么 1还是0， 判断
        n左移把右边的数字放入新变量中

'''

class Solution:
    def reverseBits(self,n):
        result = 0
        for i in range(32):
            result = (result<<1) + (n&1)
            n >>=1
        return result
    def getLastBit(self,n):
        return n&1

if __name__=="__main__":
    # 43261596    =>>  964176192
    n = 43261596
    s = Solution()
    result = s.reverseBits(n)
    print (result)

    n = 2
    result = s.getLastBit(n)
    print (result)

