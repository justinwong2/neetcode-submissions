class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [temperatures[0]]
        indexes = [0] 
        arrLength = len(temperatures)
        answers = [0] * arrLength
        if arrLength == 1:
            return answers

        for i in range(1, arrLength):
            currTemp = temperatures[i]
            #for this current temperature, check if it is higher than the previous temperaure using peek
            # if currTemperature is lower, then just add it to the stack
            # if it is higher, pop from both stacks, take i - prev index
            # keep repeating until it is no longer higher, then add this current one to the stack
            while len(stack) > 0 and currTemp > stack[-1]:
                stack.pop()
                index = indexes.pop()
                answers[index] = i - index
            stack.append(currTemp)
            indexes.append(i)
        return answers

