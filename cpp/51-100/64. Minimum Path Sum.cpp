class Solution {
public:
	int minPathSum(vector<vector<int>>& grid) {
		int m = grid.size(), n = grid[0].size();
		vector<int> prev(n + 1, 0);
		vector<int> cur(n + 1, 0);
		if(grid.empty())
			return 0;
		for(int j = 1; j < n; j++)
			grid[0][j] += grid[0][j-1];
		for(int i = 1; i < m; i++)
			grid[i][0] += grid[i-1][0];
		for(int i = 1; i <= m; i++)
		{
			for(int j = 1; j <= n; j++)
			{
				cur[j] = grid[i-1][j-1];
				if(prev[j] < cur[j-1])
					cur[j] += prev[j];
				else
					cur[j] += cur[j-1];
			}
			swap(cur, prev);
		}
		return prev[n];
	}
};
