func longestConsecutive(nums []int) int {
    counter := make(map[int]bool)
    for _, num := range nums {
        counter[num] = true
    }
    maxCount := 0
    i := 0
    for i < len(nums) {
        if !counter[nums[i]-1] {
            count := 0
            j := 0
            for counter[nums[i]+j] {
                counter[nums[i]+j] = false
                count++
                j++
            }
            if count > maxCount {
                maxCount = count
            }
        }
        i++
    }
    return maxCount
}