from collections import deque


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        def int_change(string):
            try:
                k = int(string)
                return k
            except ValueError:
                return False

        stack = []
        for i in tokens:
            if (i=="*" or i=="+" or i=="-" or i=="/"):
                right = stack.pop()
                left = stack.pop()
                operator = i
                res = 0  
                match operator:
                    case "+":
                        res = int((left) + (right))
                    case "-":
                        res = int((left) - (right)) 
                    case "*":
                        res = int((left) * (right)) 
                    case "/":
                        res = int((left)/(right))

                stack.append(res)
            else:
                stack.append(int_change(i))

        return (stack.pop())
                    

        