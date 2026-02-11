class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        sol, i, j = [], 0, 0
        while bottom >= top and right >= left:
            while j <= right:
                sol.append(matrix[i][j])
                print(sol)
                j += 1
            j -= 1
            top += 1
            i += 1
            if bottom < top or right < left:
                return sol
            while i <= bottom:
                print(i,j)
                sol.append(matrix[i][j])
                print(sol)
                i += 1
            i -= 1
            right -= 1
            j -= 1
            if bottom < top or right < left:
                return sol
            while j >= left:
                sol.append(matrix[i][j])
                print(sol)
                j -= 1
            j += 1
            bottom -= 1
            i -= 1
            if bottom < top or right < left:
                return sol
            while i >= top:
                sol.append(matrix[i][j])
                print(sol)
                i -= 1
            i += 1
            left += 1
            j += 1
        return sol

