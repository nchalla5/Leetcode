class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # def checkSquare(board, r, c, val):
        #     x, y = (r//3)*3, (c//3)*3
        #     for i in range(3):
        #         for j in range(3):
        #             if board[x+i][y+j] == val:
        #                 return False
        #     return True
        def solve(board, r, c, rowsReq, columnsReq, sReq, original):
            if len(rowsReq[8]) == len(columnsReq[8]) == 0:
                return True
            # print(r,c)
            if c > 8:
                return solve(board, r+1, 0, rowsReq, columnsReq, sReq, original)
            if original[r][c] != ".":
                return solve(board, r, c+1, rowsReq, columnsReq, sReq, original)
            for val in range(1,10):
                if str(val) in rowsReq[r] and str(val) in columnsReq[c] and str(val) in sReq[r//3][c//3]:
                    rowsReq[r].remove(str(val))
                    columnsReq[c].remove(str(val))
                    board[r][c] = str(val)
                    sReq[r//3][c//3].remove(str(val))
                    if solve(board, r, c+1, rowsReq, columnsReq, sReq, original):
                        return True
                    rowsReq[r].add(str(val))
                    columnsReq[c].add(str(val))
                    board[r][c] = "."
                    sReq[r//3][c//3].add(str(val))
            return False
                         
        original = board.copy()
        rowsReq = [set() for _ in range(9)]
        columnsReq = [set() for _ in range(9)]
        sReq = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                rowsReq[i].add(str(j+1))
                columnsReq[i].add(str(j+1))
        for i in range(3):
            for j in range(3):
                sReq[i][j].update(["1","2","3","4","5","6","7","8","9"])
        
        # print(sReq)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    # print(i//3,j//3, board[i][j])
                    rowsReq[i].remove(board[i][j])
                    columnsReq[j].remove(board[i][j])
                    sReq[i//3][j//3].remove(board[i][j])
        solve(board, 0, 0, rowsReq, columnsReq, sReq, original)
        