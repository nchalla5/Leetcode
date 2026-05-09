class Solution:
    def lowestCommonAncestor(self, root, p, q):

        current = root

        while current:

            # Both nodes lie in left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left

            # Both nodes lie in right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right

            # Split point found -> this is LCA
            else:
                return current