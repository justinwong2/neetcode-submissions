class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            try:
                stack.append(int(op))
            except ValueError:
                if op == "+":
                    t1 = stack.pop()
                    t2 = stack.pop()
                    stack.append(t2)
                    stack.append(t1)
                    stack.append(t1 + t2)
                elif op == "D":
                    t1 = stack.pop()
                    stack.append(t1)
                    stack.append(t1 * 2)
                elif op == "C":
                    stack.pop()
        
        count = 0
        for i in range(len(stack)):
            count += stack.pop()
        return count
        