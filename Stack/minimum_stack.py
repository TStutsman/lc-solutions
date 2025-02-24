class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else None