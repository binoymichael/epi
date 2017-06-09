class Stack:
    def __init__(self):
        self.stack = []


    def push(self, item):
        if self.stack:
            _, top_max = self.stack[-1]
            top_max = item if item > top_max else top_max
            self.stack.append((item, top_max))
        else:
            self.stack.append((item, item))

    def pop(self):
        item, _ = self.stack.pop()
        return item

    def __repr__(self):
        return repr(self.stack)

    def max(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


s = Stack()
print(s)
s.push(1)
s.push(2)
print(s)
print(s.pop())
print(s)
