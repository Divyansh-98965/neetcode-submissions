class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mincost = [0] * (n + 1)
        mincost[0] = cost[0]
        mincost[1] = cost[1]

        for i in range(2,n):
            mincost[i] = min(mincost[i-1],mincost[i-2]) + cost[i]

        return min(mincost[n - 2], mincost[n - 1])
