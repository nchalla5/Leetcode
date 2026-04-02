class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        rank = [0 for _ in range(n)]
        parent = [i for i in range(n)]
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                parent[px] = py
            else:
                parent[py] = px
                if rank[px] == rank[py]:
                    rank[px] += 1
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i,j)
        return len(set([find(i) for i in range(n)]))


