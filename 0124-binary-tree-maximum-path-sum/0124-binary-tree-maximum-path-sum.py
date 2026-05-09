class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Ignore negative contributions
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # Best path passing through current node
            current_path = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_path)

            # Return best single-side contribution upward
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum