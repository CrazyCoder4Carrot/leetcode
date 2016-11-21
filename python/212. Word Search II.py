class Solution(object):
    def __init__(self):
        self.root = {}
    def insert(self, string):
        node = self.root
        for c in string:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = True
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        m = len(board)
        n = len(board[0])
        def check(i, j, path, node, board):
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == "#": 
                return
            c = board[i][j]
            if c not in node:
                return
            if "#" in node[c]:
                res.append(path + c)
            path += c
            board[i][j] = "#"
            check(i+1, j, path, node[c], board)
            check(i, j+1, path, node[c], board)
            check(i-1, j, path, node[c], board)
            check(i, j-1, path, node[c], board)
            board[i][j] = c
        for word in words:
            self.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                check(i, j, "", self.root, board)
        return list(set(res))
