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
        if not root:
            return ""
        queue = [root]
        res = [str(root.val)]
        while queue:
            temp = []
            for node in queue:
                if node.left:
                    res.append(int(node.left.val))
                    temp.append(node.left)
                else:
                    res.append("Null")
                if node.right:
                    res.append(int(node.right.val))
                    temp.append(node.right)
                else:
                    res.append("Null")
            queue = temp
        return ",".join(map(str, res))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        print data
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = [root]
        index = 1
        while queue and index < len(nodes):
            temp = []
            for node in queue:
                node.left = TreeNode(int(nodes[index])) if nodes[
                    index] != "Null" else None
                index += 1
                if node.left:
                    temp.append(node.left)
                if index > len(nodes):
                    break
                node.right = TreeNode(int(nodes[index])) if nodes[
                    index] != "Null" else None
                if node.right:
                    temp.append(node.right)
                if index > len(nodes):
                    break
                index += 1
            queue = temp
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
