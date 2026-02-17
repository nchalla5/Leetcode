class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getCount(n, arr):
            count = 0
            for pile in arr:
                count += pile // n
                if pile % n != 0:
                    count += 1
            return count
        if h == len(piles):
            return max(piles)
        piles.sort()
        for i in range(len(piles)):
            if i + getCount(piles[i], piles[i:]) <= h:
                break
        left, right = 1, piles[i]
        if i != 0:
            left = piles[i-1]
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if  i + getCount(mid, piles[i:]) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans