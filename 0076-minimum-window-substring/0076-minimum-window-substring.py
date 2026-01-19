class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        map = defaultdict(int)
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0
        for char in t:
            map[char] += 1

        while end < len(s):
            if map[s[end]] > 0:
                count -= 1
            map[s[end]] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if map[s[start]] == 0:
                    count += 1
                map[s[start]] += 1
                start += 1

        return "" if min_len == float('inf') else s[start_index:start_index + min_len]