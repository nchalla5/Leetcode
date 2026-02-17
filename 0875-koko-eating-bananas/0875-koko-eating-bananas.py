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
        # print(piles)
        for i in range(len(piles)):
            # print(i,  i + getCount(piles[i], piles[i:]) )
            if i + getCount(piles[i], piles[i:]) <= h:
                break
        # print(i)
        left, right = 1, max(piles)
        if i == 0:
            left = 1
            right = piles[i]
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if  i + getCount(mid, piles[i:]) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        # if i == 0:
        #     sol = j = piles[i]
        #     while j >= 1:
        #         # print(j, i + getCount(j, piles[i:]))
        #         if i + getCount(j, piles[i:]) <= h:
        #             sol = j
        #             j -= 1
        #         else:
        #             return sol
        # else:
        #     sol = j = piles[i]
        #     while j >= piles[i-1]:
        #         # print(j, i + getCount(j, piles[i:]))
        #         if i + getCount(j, piles[i:]) <= h:
        #             sol = j
        #             j -= 1
        #         else:
        #             return sol
        # return j
        
