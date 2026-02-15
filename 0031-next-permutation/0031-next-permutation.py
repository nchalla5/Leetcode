class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        # print(nums)
        # nums[0:2].sort()
        # print(nums)
        while i >= 0:
            if i+1 == len(nums):
                i -= 1
            elif (i+1 < len(nums) and nums[i] >= nums[i+1]):
                i -= 1
            else:
                j = len(nums)-1
                while j >= 0 and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                # print(nums)
                # print(nums[i+1:][::-1])
                nums[i+1:] = nums[i+1:][::-1]
                return 
        nums[:] = nums[::-1]
        return
