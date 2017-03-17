class Solution {
public:
    int totalNQueens(int n) {
        vector<vector<string>> res;
        int count = 0;
		string row(n, '.');
		vector<string> board(n, row);
		vector<bool> flags(n, false);
		vector<bool> diag(2 * n - 1, false);
		vector<bool> anti_diag(2 * n - 1, false);
		helper(n, flags, diag, anti_diag, 0, board, res, count);
		return count;
    }
    void helper(int n, vector<bool> &flags, vector<bool> &diag, vector<bool> &anti_diag, int level, vector<string> &board, vector<vector<string>> &res, int &count)
	{
		if (level == n)
		{
			count += 1;
			return ;
		}
		for (int i = 0; i < n; i++)
		{
			if (flags[i] || diag[n - level - 1 + i] || anti_diag[level + i])
				continue;
			board[level][i] = 'Q';
			flags[i] = diag[n - level - 1 + i] = anti_diag[level + i] = true;
			helper(n, flags, diag, anti_diag, level + 1, board, res, count);
			flags[i] = diag[n - level - 1 + i] = anti_diag[level + i] = false;
			board[level][i] = '.';
		}
	}
};