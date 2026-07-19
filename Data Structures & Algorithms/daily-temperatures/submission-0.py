class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force approach
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            j = i
            for j in range(i,n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                

        return res



