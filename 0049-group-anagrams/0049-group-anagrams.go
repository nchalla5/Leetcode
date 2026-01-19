func groupAnagrams(strs []string) [][]string {
    groupsMap := map[string][]string{}

    for _, str := range strs {
        cl := class(str)
        groupsMap[cl] = append(groupsMap[cl], str)
    }

    groups := make([][]string, 0, len(groupsMap))
    for _, strs := range groupsMap {
        groups = append(groups, strs)
    }

    return groups
}

func class(str string) string {
    bz := []byte(str)
    slices.Sort(bz)
    return string(bz)
}