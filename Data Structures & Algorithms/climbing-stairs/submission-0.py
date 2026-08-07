class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        ways = [0,1,2]

        for i in range(3,n + 1):
            ways.append(ways[i - 1] + ways[i - 2])

        return ways[n]

