class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # def find(i, buy, cap):
        #     if cap == 0:
        #         return 0
        #     if i == len(prices):
        #         return 0
        #     if buy:
        #         return max(find(i+1, 1, cap), find(i+1, 0, cap-1)+prices[i])
        #     return max(find(i+1, 0, cap), find(i+1, 1, cap)-prices[i])
        # return find(0,0,2)
        n = len(prices)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(1,-1,-1):
                for cap in range(1,3):
                    if buy:
                        dp[i][buy][cap] = max(dp[i+1][buy][cap], dp[i+1][0][cap-1]+prices[i])
                    else:
                        dp[i][buy][cap] = max(dp[i+1][buy][cap], dp[i+1][1][cap]-prices[i])
        return dp[0][0][2]