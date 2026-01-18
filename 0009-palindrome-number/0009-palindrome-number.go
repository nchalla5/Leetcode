func isPalindrome(x int) bool {
    if x < 0 {
        return false
    }
    str := strconv.Itoa(x)
    l, r := 0, len(str)-1
    for l < r {
        if str[l] != str[r] {
            return false
        }
        l++
        r--
    }
    return true
}