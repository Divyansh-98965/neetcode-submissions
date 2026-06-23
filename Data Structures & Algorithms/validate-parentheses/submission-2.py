from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in s:

            if (i == '(' or i == '{' or i == '['):
                stack.append(i)

            elif (i == ')' or i == '}' or i == ']'):

                if not stack:
                    return False 

                top = stack[-1]

                if ((i == ')' and top != '(') or (i == '}' and i == '{') or (i == ']' and top != '[')):
                    return False

                stack.pop()

        return len(stack) == 0