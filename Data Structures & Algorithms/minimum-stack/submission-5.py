class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.currMin = None

    def push(self, val: int) -> None:
        self.s1.append(val)
        if self.currMin is None or val <= self.currMin:
            self.s2.append(val)
            self.currMin = val

    def pop(self) -> None:
        val = self.s1.pop()
        if self.currMin is not None and self.s2[-1] == val:
            self.s2.pop()
            if len(self.s2) == 0:
                self.currMin = None
            else:
                self.currMin = self.s2[-1]

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        if len(self.s2) == 0:
            return None
        return self.s2[-1]
        
