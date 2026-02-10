# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root, target, path):
            if root is None or root.val == target:
                return
            if root.val < target:
                path.append(root)
                return findPath(root.right, target, path)
            else:
                path.append(root)
                return findPath(root.left, target, path)
        path1, path2 = [], []
        findPath(root, p.val, path1)
        path1.append(p)
        findPath(root, q.val, path2)
        path2.append(q)
        sol = root.val
        i = 0
        while i < len(path1) and i < len(path2) and path1[i].val == path2[i].val:
            i += 1
        # print(path1, path2)
        i -= 1
        return path1[i]

        