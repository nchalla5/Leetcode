class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        stack.append(0)
        sol = 0
        for i in range(len(height)):
            if height[i] < stack[-1]:
                stack.append(height[i])
            else:
                j = len(stack) - 1
                while j >= 0 and stack[j] < height[i]:
                    j -= 1
                if j<0:
                    j = 0
                level = min(height[i], stack[j])
                j += 1
                while j < len(stack):
                    sol += level - stack[j]
                    stack[j] = level
                    j += 1
                # print(stack, height[i], level)
                if stack[0] <= height[i]:
                    stack.clear()
                    stack.append(height[i])
                else:
                    stack.append(height[i])
            # print(stack, sol)
        return sol
            