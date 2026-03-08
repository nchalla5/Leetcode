class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(1,-1,-1):
                for cap in range(1,k+1):
                    if buy:
                        dp[i][buy][cap] = max(dp[i+1][buy][cap], dp[i+1][0][cap-1]+prices[i])
                    else:
                        dp[i][buy][cap] = max(dp[i+1][buy][cap], dp[i+1][1][cap]-prices[i])
        return dp[0][0][k]