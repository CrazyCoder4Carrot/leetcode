class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.counter = [0] * (2 * n + 2)
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        inc = 1 if player == 1 else -1
        self.counter[col] += inc
        self.counter[row + self.n] += inc
        if row == col:
            self.counter[-2] += inc
        if (row + col) == (self.n - 1):
            self.counter[-1] += inc
        if abs(self.counter[-1]) == self.n:
            return player
        if abs(self.counter[-2]) == self.n:
            return player
        if abs(self.counter[col]) == self.n:
            return player
        if abs(self.counter[row + self.n]) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
