from collections import deque

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

        def dfs(root, encoded_str):
            if root is None:
                encoded_str.append(",")
                return
            encoded_str.append(str(root.val))
            dfs(root.left, encoded_str)
            dfs(root.right, encoded_str)

        encoded_str = deque()
        dfs(root, encoded_str)

        return " ".join(encoded_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(idx, data):
            if data[idx] == ",":
                return None, idx
            new_node = TreeNode()
            new_node.val = int(data[idx])
            new_node.left, idx_end = dfs(idx + 1, data)
            new_node.right, idx_end = dfs(idx_end + 1, data)
            return new_node, idx_end

        root, _ = dfs(0, data.split(" "))
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
