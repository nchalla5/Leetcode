class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >= 0:
            # I am trying to find out the first digit that not in descending order
            if i+1 == len(nums):
                i -= 1
            elif (i+1 < len(nums) and nums[i] >= nums[i+1]):
                i -= 1
            else:
                # swap it with the first digit from end thats greater than it.
                j = len(nums)-1
                while j >= 0 and nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                # The remaining elements should be in descending order now
                # So reverse all the elements after i to get the next perm in sequence
                nums[i+1:] = nums[i+1:][::-1]
                return 
        nums[:] = nums[::-1]
        return
