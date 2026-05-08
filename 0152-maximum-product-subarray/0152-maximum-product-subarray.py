class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd, sol = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            temp = maxProd
            maxProd = max(nums[i], maxProd*nums[i], minProd*nums[i])
            minProd = min(nums[i], minProd*nums[i], temp*nums[i])
            sol = max(maxProd, sol)
        return sol


            