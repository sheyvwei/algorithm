'''
 * [20] Valid Parentheses
 *
 * https://leetcode.com/problems/valid-parentheses/description/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
给定一个只包含字符'（'，'）'，'{'，'}'，'['和']'的字符串，确定输入字符串是否有效。
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
思路： 入栈和出栈，字典。。。仅涉及到3对字符，可以用map保存
'''

class Solution:
    def isValid(self, s):
        stack = []
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for x in s:
            if x in map:
                #左括号入栈
                stack.append(map[x])
            else:
                #不在map中表示是右括号,右括号出栈
                #长度大于0出栈
                if(len(stack)!= 0):
                    top_element = stack.pop()
                    if top_element != x:
                        return False
                    else:
                        continue
                else:
                    return False
                ## 避免存在只有左括号
        return len(stack) == 0

if __name__ == '__main__':
    str = "()"
    s = Solution()
    result = s.isValid(str)
    print (result)






















