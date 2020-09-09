class Solution:
    def twoCitySchedCost(self, cost: List[List[int]]) -> int:
        n = len(cost) // 2
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + cost[i - 1][0]
        for i in range(1, n+1):
            dp[0][i] = dp[0][i - 1] + cost[i - 1][1]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j] + cost[i + j - 1][0], dp[i][j - 1] + cost[i + j - 1][1])
        return dp[-1][-1]
