class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        count = 1
        result = [0] * len(temperatures)


        for i in temperatures:
            stack.append(i)

        while len(stack) > 1:
            if stack[-1] < stack[-count]: 
                result[-count] = count
                stack.pop()
            else:
                count += 1

        return result
            
            




        