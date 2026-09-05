class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case '+':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    val = val1 + val2
                    stack.append(val)
                case '-':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    val = val1 - val2
                    stack.append(val)
                case '*':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    val = val1 * val2
                    stack.append(val)
                case '/':
                    val2 = stack.pop()
                    val1 = stack.pop()
                    val = int(val1 / val2)
                    stack.append(val)
                case _:
                    stack.append(int(i))

        fin = stack.pop()
        return fin