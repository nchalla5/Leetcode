func isAnagram(s string, t string) bool {
    smap := make(map[rune]int)
    if len(s) != len(t) {
        return false
    }
    for _, char := range s {
        smap[char]++
    }
    // count := 1
    for _, char := range t {
        if smap[char] == 0{
            return false
        }
        smap[char]--
    }
    return true
}