'''
Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.
给定一个具有偶数长度的整数数组，其中该数组中的不同数字代表不同种类的糖果。每个数字表示一个相应种类的糖果。您需要将这些糖果在数量上平均分配给兄弟姐妹。返回姐姐可能获得的最大种类的糖果
Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
The sister has three different kinds of candies.
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
The sister has two different kinds of candies, the brother has only one kind of candies.
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].

思路： 要数量一样，所以最多 n/2的数量，即糖果种类是多少
'''

class Solution:
    def distributeCandies(self,candies):
        length = len(set(candies))
        return min(length,(len(candies)/2))
    #   return min(len(set(candies)),len(candies) >>1)  右移等于除以2

if __name__=="__main__":
    s = Solution()
    candies = [1, 1, 2, 3]
    print (s.distributeCandies(candies))