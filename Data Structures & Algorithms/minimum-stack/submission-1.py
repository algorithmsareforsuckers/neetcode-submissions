class MinStack:

    def __init__(self):
        self.mini = None
        self.prev = []
        self.stack = []

    def push(self, val: int) -> None:
        if self.mini is None:
            self.mini = val
        elif val <= self.mini:
            self.prev.append(self.mini)
            self.mini = val
        self.stack.append(val)
        
        

    def pop(self) -> None:
        if self.mini == self.stack[-1]:
            if len(self.stack) == 1:
                self.mini = None
            else:
                self.mini = self.prev[-1]
                self.prev.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini
        
