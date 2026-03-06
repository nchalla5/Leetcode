class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol = 0
        minn = prices[0]
        for i in prices:
            if i < minn:
                minn = i
            elif i - minn > sol:
                sol = i - minn
        return sol