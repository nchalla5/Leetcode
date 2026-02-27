class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        def checkNode(node, col, color, adjMat):
            for it in adjMat[node]:
                if color[it] != 0 and col == color[it]:
                    return False
            return True
        def colorNodes(adjMat, node, colors):
            if node == n+1:
                return True
            for i in range(1,node+1):
                if checkNode(node, i, colors, adjMat):
                    colors[node] = i
                    if colorNodes(adjMat, node+1, colors):
                        return True
                    colors[node] = 0
            return False
            
        adjMat = [[] for _ in range(n+1)]
        for path in paths:
            adjMat[path[0]].append(path[1])
            adjMat[path[1]].append(path[0])
        colors = [0]*(n+1)
        colorNodes(adjMat, 1, colors)
        return colors[1:]