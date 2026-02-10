# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorderList = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            inorderList.append(root.val)
            inorder(root.right)
        inorder(root)
        for i in range(0,len(inorderList)-1):
            if inorderList[i] >= inorderList[i+1]:
                return False
        return True

            
        