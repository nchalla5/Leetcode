class Solution:
    def romanToInt(self, s: str) -> int:
        toInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # prev = s[0]
        sol = toInt[s[0]]
        for i in range(1,len(s)):
            if toInt[s[i-1]] < toInt[s[i]]:
                sol -= 2*toInt[s[i-1]]
            sol += toInt[s[i]]
        return sol

        