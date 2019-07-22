'''
551.学生出席记录，缺席A:Absent,迟到L:Late, 出席P: Present,一个学生记录不能超过1个A和2个连续的L
eg:     "PPALLP" ---- TRUE
        "PPALLL"----false  超过2个L
'''

class Solution:
    def IsAttendanceRecord(self, record):
        '''
        :param record: str
        :return: bool
        '''
        a = 0
        p = 0
        for (key,value) in enumerate(record):
            if(value == 'A'):
                a += 1
            if (a > 1):
                return False
            if( (key + 2) < (len(record)) and value == 'L' and record[key+1] == 'L' and record[key+2] == "L"):
                return False
        return True



if __name__ == '__main__':
    s = Solution()
    record = "PPALLL"
    # Solution.IsAttendanceRecord(l)
    print (s.IsAttendanceRecord(record))