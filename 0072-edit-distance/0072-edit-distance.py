class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word2)
        n = len(word1)
        lcs = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            lcs[i][0] = i
        for j in range(1, n + 1):
            lcs[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word2[i-1] == word1[j-1]:
                    lcs[i][j] = lcs[i-1][j-1]
                else:
                    lcs[i][j] = 1 + min(lcs[i-1][j], lcs[i][j-1], lcs[i-1][j-1])
        # print(lcs)
        return lcs[-1][-1]

        