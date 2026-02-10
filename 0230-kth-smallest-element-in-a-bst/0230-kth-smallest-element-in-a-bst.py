# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sol = []
        def findk(root):
            if root is None:
                return 
            findk(root.left)
            sol.append(root.val)
            findk(root.right)
        findk(root)
        return sol[k-1]

