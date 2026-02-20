class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def printPuzzle(sol):
            final = []
            for i in range(len(sol)):
                curr = []
                for j in range(len(sol[0])):
                    row = ""
                    for k in range(len(sol[0])):
                        if sol[i][j] == k:
                            row += "Q"
                        else:
                            row += "."
                    curr.append(row)
                final.append(curr)
            return final

        def diagCheck(arr, r, i):
            x = 1
            while r-x >= 0:
                if r >= x and (arr[r-x] == i+x or arr[r-x] == i-x):
                    return False
                x += 1
            return True

        def backTrack(arr, r, sol):
            if r == n:
                sol.append(arr.copy())
                return
            for i in range(0,n):
                if i not in arr and diagCheck(arr, r, i):
                    arr[r] = i
                    backTrack(arr, r+1, sol)
                    arr[r] = -1
        arr = [-1]*n
        sol = []
        backTrack(arr, 0, sol)
        # print(sol)
        return printPuzzle(sol)
        