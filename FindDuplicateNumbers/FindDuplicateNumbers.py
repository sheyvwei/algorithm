'''
    数组中重复的数字：
    在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。
    数组中某些数字是重复的，但不知道有几个数字是重复的，也不知道每个数字重复几次。
    请找出数组中任意一个重复的数字
    Input:
    {2, 3, 1, 0, 2, 5}

    Output:
    2
'''

class Solution:
    def boolDuplicate(self,numbers,length,result):

        if(length == 0):
            return False
        for i in numbers:
            while(numbers[i] != i):
                print(numbers[i])
                if numbers[i] == numbers[numbers[i]]:
                    result[0] = numbers[i]
                    return False
                self.swap(numbers, i, numbers[i])
        return False;
    def swap(self,nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

if __name__ == '__main__':
    numbers = [2, 3, 1, 0, 2, 5]
    s = Solution()
    result  = []
    s.boolDuplicate(numbers,len(numbers),result)
    print (len(result))

