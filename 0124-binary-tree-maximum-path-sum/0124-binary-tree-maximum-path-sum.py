# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recur(root):
            if not root:
                return None
            c1 = recur(root.left)
            c2 = recur(root.right)
            if c1 and c2:
                s = root.val + max(c1[0], c2[0], 0)
                d = root.val + c1[0] + c2[0]
                p = max(c1 + c2)
                return [s,d,p]
            elif c1:
                s = root.val + max(c1[0], 0)
                d = root.val + max(c1[0], 0)
                p = max(c1)
                return [s,d,p]
            elif c2:
                s = root.val + max(c2[0], 0)
                d = root.val + max(c2[0], 0)
                p = max(c2)
                return [s,d,p]
            else:
                s = root.val
                d = root.val
                p = root.val
                return [s,d,p]
        return max(recur(root))