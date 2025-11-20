class StackOnList():
    def __init__(self):
        self.stack = []
    def push(self, x):
        if not self.stack:
            current_min = x
        else:
            current_min = min(x, self.stack[-1][1])
        self.stack.append((x, current_min))
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Empty stack")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1][0]
        raise IndexError("Empty stack")
    def is_empty(self):
        return len(self.stack) == 0
    def __len__(self):
        return len(self.stack)
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1 ]
        raise IndexError("Empty stack")
class QueueOnList:
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Empty queue")
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Empty queue")
    def is_empty(self):
        return len(self.queue) == 0
    def __len__(self):
        return len(self.queue)