func lengthOfLongestSubstring(s string) int {
    counts := make(map[byte]int)
    start, sol := -1,1
    i, n := 1, len(s)
    if n == 0 {
        return 0
    }
    counts[s[0]] = 0
    for i<n {
        j, ok := counts[s[i]]
        if ok {
            if i-start-1 > sol {
                sol = i-start-1
            }
            for start < j {
                start++
                delete(counts, s[start])
            }
        }
        counts[s[i]] = i
        i++
    }
    if i-start-1 > sol {
        sol = i-start-1
    }
    return sol
}