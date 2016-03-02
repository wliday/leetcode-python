class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or curMin > x:
            curMin = x
        self.stack.append((x, curMin))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        