class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        def myFunc(board, word, check, i, j, k):
            # print(word[k])
            up = False
            down = False
            left = False
            right = False
            if k == len(word)-1:
                return True
            if i>0:
                if check[i-1][j] == 0 and board[i-1][j] == word[k+1]:
                    check[i-1][j] = 1
                    up = myFunc(board, word, check, i-1, j, k+1)
                    check[i-1][j] = 0
            if j>0:
                if check[i][j-1] == 0 and board[i][j-1] == word[k+1]:
                    check[i][j-1] = 1
                    left = myFunc(board, word, check, i, j-1, k+1)
                    check[i][j-1] = 0
            if i<len(board)-1:
                if check[i+1][j] == 0 and board[i+1][j] == word[k+1]:
                    check[i+1][j] = 1
                    down = myFunc(board, word, check, i+1, j, k+1)
                    check[i+1][j] = 0
            if j<len(board[0])-1:
                if check[i][j+1] == 0 and board[i][j+1] == word[k+1]:
                    check[i][j+1] = 1
                    right = myFunc(board, word, check, i, j+1, k+1)
                    check[i][j+1] = 0
            return up or left or down or right

        check = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:  
                    #check = [[0 for j in range(len(board[0]))] for i in range(len(board))]
                    check[i][j] = 1
                    res = res or myFunc(board, word, check, i, j, 0)
                    check[i][j] = 0
        return res

        


        