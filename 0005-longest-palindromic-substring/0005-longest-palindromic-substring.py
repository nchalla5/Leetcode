class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        sol = s[0:1]
        solLen = 1
        for i in range(1, len(s)):
            j = i-1
            k = i
            if solLen%2 == 0:
                t = (solLen//2) - 1
            else:
                t = ((solLen+1)//2) - 1
            # print(i,j,k,t,s[j-t:k+t+1],s[j-t:k+t+1][::-1], sol)
            if j-t >= 0 and k+t < len(s) and s[j-t:k+t+1] == s[j-t:k+t+1][::-1]:
                while j-t >= 0 and k+t < len(s) and s[j-t] == s[k+t]:
                    t += 1
                # print(t)
                t -= 1
                sol = s[j-t:k+t+1]
                solLen = len(sol)

            j = i-1
            k = i+1
            if solLen%2 == 0:
                t = (solLen//2) - 1
            else:
                t = ((solLen-1)//2) - 1
                # print(solLen,sol,t)
            # print(i,j,k,t,s[j-t:k+t+1],s[j-t:k+t+1][::-1], sol, solLen )
            if j-t >= 0 and k+t < len(s) and s[j-t:k+t+1] == s[j-t:k+t+1][::-1]:
                while j-t >= 0 and k+t < len(s) and s[j-t] == s[k+t]:
                    t += 1
                t -= 1
                # print(t)
                sol = s[j-t:k+t+1]
                solLen = len(sol)
        return sol


        