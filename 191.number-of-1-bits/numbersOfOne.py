'''
    无符号二进制数字中1的个数

Example 1:
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

 思路：  1.用 n&1 去n的最后一位，再右移动
        2. 或者 n & (n-1)   可以去除 n的最后 一个 1 ， 比如  n为  B(11)  n&(n-1) 变为 10

'''

class Solution:
    def hammingWeight(self, n):
        count = 0
        while(n):
            if n&1 == 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight2(self,n):
        count = 0
        while n:
            n &= n-1
            count += 1
        return count

if __name__=="__main__":
    n = 3
    n = 4294967293
    s = Solution()
    result = s.hammingWeight(n)
    print (result)
    n = 3
    result = s.hammingWeight2(n)
    print(result)

    n = 5   #  110   >>   100
    n = n&(n-1)
    print (n)
