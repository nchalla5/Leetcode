func canFinish(numCourses int, prerequisites [][]int) bool {
    edges := make(map[int][]int)
    indegree := make([]int, numCourses)
    for _, prereq := range prerequisites {
        edges[prereq[1]] = append(edges[prereq[1]], prereq[0])
        indegree[prereq[0]]++
    }
    queue := []int{}
    for i := 0; i<numCourses; i++ {
        if indegree[i] == 0 {
            queue = append(queue, i)
        }
    }
    completed := 0
    for len(queue) > 0 {
        pop := queue[len(queue)-1]
        queue = queue[:len(queue)-1]
        completed++
        for _, edge := range edges[pop] {
            indegree[edge]--
            if indegree[edge] == 0 {
                queue = append(queue, edge)
            }
        }
    }
    if completed == numCourses {
        return true
    }
    return false
}