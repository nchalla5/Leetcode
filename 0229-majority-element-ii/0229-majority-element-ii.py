class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        common = counts.most_common(3)
        sol = []
        for comm in common:
            if comm[1] > len(nums) // 3:
                sol.append(comm[0])
        return sol