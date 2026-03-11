class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            inDegree[prereq[0]] += 1
        curr = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                curr.append(i)
        sol = []
        while len(curr) > 0:
            c = curr.pop()
            sol.append(c)
            for neigh in graph[c]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    curr.append(neigh)
        if len(sol) == numCourses:
            return sol
        else:
            return []