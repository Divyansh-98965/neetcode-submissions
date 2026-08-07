class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.array = [0] * (n + 1) 
        self.array[1] = 1
        self.array[2] = 2

        for i in range(3,n + 1,1):
            self.array[i] = self.array[i - 1] + self.array[i - 2]

        return self.array[n]

