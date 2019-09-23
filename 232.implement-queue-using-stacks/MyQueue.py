'''

用栈实现队列的以下操作
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
思路： 队列特性：先进先出
    所以该题为用栈实现先进先出的队列功能
'''


class MyQueue:
    def __init__(self):
        self.stack = []
        self.help_stack = []
    def push(self,x):
        while self.stack:
            self.help_stack.append(self.stack.pop())
        self.help_stack.append(x)
        while self.help_stack:
            self.stack.append(self.help_stack.pop())

    def pop(self):
        return self.stack.pop()
    def peek(self):
        # 获取头元素
        return self.stack[-1]
    def empty(self):
        return not bool(self.stack or self.help_stack)

if __name__=="__main__":
    s = MyQueue()
    s.push(1)
    s.push(2)
    s.push(3)
    result = s.pop()
    print (result)

