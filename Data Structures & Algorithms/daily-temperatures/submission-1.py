class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force approach
        # n = len(temperatures)
        # res = [0] * n
        # for i in range(n):
        #     j = i
        #     for j in range(i,n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i
        #             break
        # return res

        # optimized approach
        n = len(temperatures)
        result = [0]*n
        stack = []  # Will store pairs of [temperature, index]
        
        for i, t in enumerate(temperatures):
            # While the stack is not empty AND the current temperature 
            # is hotter than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                result[stack_i] = i - stack_i  # Calculate the distance gap
                
            # Push the current temperature and its index onto the stack
            stack.append([t, i])
            
        return result
                
            