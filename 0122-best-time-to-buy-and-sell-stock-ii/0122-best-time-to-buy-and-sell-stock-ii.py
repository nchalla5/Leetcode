class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, high, sol, temp = prices[0], prices[0], 0, 0
        for i in prices:
            if i > high:
                high = i
                temp = high - low
            elif i < high:
                sol += temp
                temp, low, high = 0, i, i
        sol += temp
        return sol