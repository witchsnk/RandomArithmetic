class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        return self.stack.pop()

    def top(self):
        """
        取栈顶
        """
        return self.stack[-1]
    def empty(self):
        return len(self.stack) == 0