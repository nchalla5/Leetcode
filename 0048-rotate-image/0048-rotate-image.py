class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(nums)
        m = len(nums[0])

        # Transpose
        for i in range(n):
            for j in range(i, m):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        
        # Reverse each row
        for i in range(n):
            left = 0
            right = n-1
            while left < right:
                temp = nums[i][left]
                nums[i][left] = nums[i][right]
                nums[i][right] = temp
                left += 1
                right -= 1
        
        return nums