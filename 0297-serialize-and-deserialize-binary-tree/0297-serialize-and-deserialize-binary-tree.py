# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "null"
        sol = []
        queue = deque([root])
        while len(queue) > 0:
            # print(queue)
            curr = queue.popleft()
            if curr is None:
                sol.append("null")
                continue
            sol.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        final = ",".join(sol)
        # print(final)
        return final

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "null":
            return None
        nodes = data.split(',')
        sol = TreeNode(nodes[0])
        i = 0
        queue = deque([sol])
        while len(queue) > 0 and i < len(nodes):
            curr = queue.popleft()
            if curr is None:
                continue
            i += 1
            if i == len(nodes):
                break
            left = nodes[i]
            if left == "null":
                curr.left = None
            else:
                curr.left = TreeNode(int(left))
            queue.append(curr.left)
            i += 1
            if i == len(nodes):
                break
            right = nodes[i]
            if right == "null":
                curr.right = None
            else:
                curr.right = TreeNode(int(right))
            queue.append(curr.right)
        return sol
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))