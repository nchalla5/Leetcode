class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        rob = [0]*n
        rob[0] = nums[0]
        rob[1] = max(nums[1], nums[0])
        for i in range(2,n):
            rob[i] = max(rob[i-1], rob[i-2] + nums[i])
        return max(rob[-1], rob[-2])

        