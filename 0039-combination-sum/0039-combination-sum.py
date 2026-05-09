from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                res.append(path[:])  # found a valid combination
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # pruning since array is sorted

                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  # reuse same number
                path.pop()  # undo choice

        backtrack(0, target, [])
        return res