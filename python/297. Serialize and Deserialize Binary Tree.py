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
            return []
        stack = [root]
        data = []
        while stack:
            levelstack = []
            for node in stack:
                if node:
                    data.append(node.val)
                    levelstack.append(node.left)
                    levelstack.append(node.right)
                else:
                    data.append('#')
            stack = levelstack
        i = len(data) - 1
        while i >= 0:
            if data[i] == '#':
                del data[i]
                i-=1
            else:
                return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data[0])
        stack = [root]
        i = 1
        while stack:
            levelstack = []
            for node in stack:
                node.left = TreeNode(data[i]) if i < len(data) and data[i] != "#" else None
                i += 1
                if node.left:
                    levelstack.append(node.left)
                node.right = TreeNode(data[i]) if i < len(data) and data[i] != "#" else None
                i += 1
                if node.right:
                    levelstack.append(node.right)
            stack = levelstack
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))