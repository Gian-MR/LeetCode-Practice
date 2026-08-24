"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = { ")" : "(", "]" : "[", "}" : "{" }
                
        for c in s:
            if c in close_open:
                if(stack and stack[-1] == close_open[c]):
                    stack.pop()

                else:
                    return False

            else:
                stack.append(c)
        
        return len(stack) == 0
"""

"""
The plan of this was to use a stack to keep track of the opening brackets. For each closing bracket, we check if it matches the most recent opening bracket. If it does, we pop the opening bracket from the stack. If it doesn't, or if there are no opening brackets left, we return False. If we finish processing the string and the stack is empty, we return True.
"""