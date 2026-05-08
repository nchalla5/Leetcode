class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax, totMax = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            t = currMax
            currMax = max(nums[i], currMax*nums[i], currMin*nums[i])
            currMin = min(nums[i], t*nums[i], currMin*nums[i])
            totMax = max(totMax, currMax)
        return totMax