'''
https://leetcode.com/problems/merge-sorted-array/description/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
题目描述 给定两个排序的整数数组nums1和nums2，将nums2合并为nums1作为一个排序的数组
Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

思路：  合理利用 m和n
        从后面 插入第二个数组的数据， 一个current指针先指向最后一个位置(m+n-1)，
        比较m,n位置之前的值，哪个大就把它放入current位置，
        需要考虑 m 或者n为0时，另一个数组要怎么放入数组1中
        continue is important
'''


class Solution:
    def merge(self,nums1,m,nums2,n):
        current = m + n -1
        while current >= 0:

            #如果m的数据用完，便于理解（在原来数组处理，所以可以不用这情况)
            if m < 1:
                # javascript使用自减运算符简化: nums1[--curent] = nums2[--n]
                n -= 1
                nums1[current] = nums2[n]
                current -=1
                continue
            # n的数组值用完
            if n < 1:
                m -= 1
                nums1[current] = nums1[m]
                current -=1
                continue
            if n == 0:
                return
            if nums1[m-1] < nums2[n-1]:
                n -= 1
                nums1[current] = nums2[n]
                current -= 1
            else:
                m -= 1
                nums1[current] = nums1[m]
                current -=1

if __name__=="__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3

    # nums1 = [1]
    # m=1
    # nums2 = []
    # n = 0
    s = Solution()
    s.merge(nums1,m, nums2, n)
    for temp in nums1:
        print (temp)


