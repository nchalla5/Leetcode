from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):

            # Overlap found -> remove current interval
            if intervals[i][0] < prev_end:
                removals += 1

            else:
                # Keep interval and update ending boundary
                prev_end = intervals[i][1]

        return removals