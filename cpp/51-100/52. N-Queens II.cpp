class Solution {
public:
    int totalNQueens(int n) {
        int count = 0;
		vector<bool> flags(n, false);
		vector<bool> diag(2 * n - 1, false);
		vector<bool> anti_diag(2 * n - 1, false);
		helper(n, flags, diag, anti_diag, 0, count);
		return count;
    }
    void helper(int n, vector<bool> &flags, vector<bool> &diag, vector<bool> &anti_diag, int level, int &count)
	{
		if (level == n)
		{
			count++;
			return ;
		}
		for (int i = 0; i < n; i++)
		{
			if (flags[i] || diag[n - level - 1 + i] || anti_diag[level + i])
				continue;
			flags[i] = diag[n - level - 1 + i] = anti_diag[level + i] = true;
			helper(n, flags, diag, anti_diag, level + 1, count);
			flags[i] = diag[n - level - 1 + i] = anti_diag[level + i] = false;
		}
	}
};