class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        #i want the first ever element pushed in stack 1
        #rest can go to stack 2
        if len(self.s1) == 0:
            self.s1.append(x)
        else:
            self.s2.append(x)

    def pop(self) -> int:
        #first element is in stack 1, pop it
        temp = self.s1.pop()
        arr = []
        #for the rest of the elements in stack2, pop all until the last, last goes to stack 1, and then everything goes back in 
        if len(self.s2) > 0:
            for i in range(len(self.s2) - 1):
                arr.append(self.s2.pop())
            
            self.s1.append(self.s2.pop())
            for i in range(len(arr)):
                self.s2.append(arr.pop())
        return temp
        

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        if len(self.s1) + len(self.s2) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()