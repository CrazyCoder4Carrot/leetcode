class Solution {
public:
	bool exist(vector<vector<char>>& board, string word) {
		if (word.empty())
			return true;
		if (board.empty())
			return false;
		int m = board.size();
		int n = board[0].size();
		bool res = false;
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
					if(dfs(i, j, m, n, board, 0, word))
						return true;
		return false;
	}
	bool dfs(int i, int j, int m, int n, vector<vector<char>>& board, int index, string word)
	{
		bool res = false;
		if (board[i][j] != word[index])
			return false;
		if (index == word.size() - 1)
		{
			return true;
		}
		char temp = board[i][j];
		board[i][j] = '*';
		if(i > 0) 
			res = dfs(i - 1, j, m, n, board, index + 1, word);
		if(!res && i < m - 1)
			res = dfs(i + 1, j, m, n, board, index + 1, word);
		if(!res && j > 0)
			res = dfs(i, j - 1, m, n, board, index + 1, word);
		if(!res && j < n - 1)
			res = dfs(i, j + 1, m, n, board, index + 1, word);
		board[i][j] = temp;
		return res;
	}
};