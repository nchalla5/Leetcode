class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        sol = []
        # print(nums)
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                j = i+1
                k = n - 1
                while j<n and k>j:
                    temp = nums[i] + nums[j] + nums[k]
                    # print(i,j,k,temp)
                    if temp == 0:
                        sol.append([nums[i],nums[j],nums[k]])
                        j += 1
                        while j <n and nums[j] == nums[j-1]:
                            j += 1
                        k -= 1
                        while k>j and nums[k] == nums[k+1]:
                            k -= 1
                    elif temp < 0:
                        j += 1
                        while j <n and nums[j] == nums[j-1]:
                            j += 1
                    else:
                        k -= 1
                        while k>j and nums[k] == nums[k+1]:
                            k -= 1
        return sol

