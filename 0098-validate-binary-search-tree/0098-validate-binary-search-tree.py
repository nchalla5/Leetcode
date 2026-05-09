class Solution:
    def isValidBST(self, root) -> bool:

        def dfs(node, low, high):
            if not node:
                return True

            # Current node must satisfy valid BST range
            if not (low < node.val < high):
                return False

            # Left subtree gets upper bound as current node
            left_valid = dfs(node.left, low, node.val)

            # Right subtree gets lower bound as current node
            right_valid = dfs(node.right, node.val, high)

            return left_valid and right_valid

        return dfs(root, float('-inf'), float('inf'))