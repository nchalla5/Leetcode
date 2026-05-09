class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            # Compute total hours needed at speed mid
            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            # If feasible, try to find a smaller valid speed
            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                # Otherwise, increase speed
                left = mid + 1

        return ans