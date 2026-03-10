class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def burst(i,j,nums, dp):
            if i>j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            sol = 0
            for ind in range(i,j+1):
                val = nums[i-1]*nums[ind]*nums[j+1] + burst(i,ind-1,nums,dp) + burst(ind+1,j,nums,dp)
                if val > sol:
                    sol = val
            dp[i][j] = sol
            return dp[i][j]
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n+1)]
        nums = [1]+nums+[1]
        return burst(1,n,nums, dp)
        