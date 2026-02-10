# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def parse(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            elif tree1 is None:
                return False
            elif tree2 is None:
                return False
            if tree1.val == tree2.val:
                return parse(tree1.left, tree2.left) and parse(tree1.right, tree2.right)
            else:
                return False
        queue = deque()
        queue.append(root)
        while len(queue)>0:
            curr = queue.popleft()
            if curr == None:
                continue
            if curr.val == subRoot.val and parse(curr, subRoot):
                return True
            queue.append(curr.left)
            queue.append(curr.right)
        return False