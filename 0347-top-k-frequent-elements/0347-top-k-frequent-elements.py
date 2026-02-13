class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)                     # O(n)
        buckets = [[] for _ in range(len(nums) + 1)]

        for x, c in freq.items():                # O(unique)
            buckets[c].append(x)

        res = []
        for c in range(len(nums), 0, -1):        # O(n)
            for x in buckets[c]:
                res.append(x)
            if len(res) == k:
                return res
        return res
        