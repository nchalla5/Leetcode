# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root is None:
            return []
        queue.append(root)
        levels = []
        while len(queue) > 0:
            currLevel = []
            tempqueue =[]
            for node in queue:
                currLevel.append(node.val)
                if node.left is not None:
                    tempqueue.append(node.left)
                if node.right is not None:
                    tempqueue.append(node.right)
            levels.append(currLevel)
            queue = tempqueue
        return levels

        