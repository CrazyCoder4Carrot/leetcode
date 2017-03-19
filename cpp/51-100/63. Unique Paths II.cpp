class Solution {
public:
	int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
		vector<vector<int >> res;
		int m = obstacleGrid.size();
		int n = obstacleGrid[0].size();
		if (obstacleGrid.empty())
			return 0;
		for (int i = 0; i <= obstacleGrid.size(); i++)
		{
			vector<int> row(obstacleGrid[0].size() + 1, 0);
			res.push_back(row);
		}
		if (obstacleGrid[0][0] != 1) {
			if (obstacleGrid.size() < obstacleGrid[0].size())

				res[1][0] = 1;
			else
				res[0][1] = 1;
		}

		for (int i = 1; i <= obstacleGrid.size(); i++)
		{
			for (int j = 1; j <= obstacleGrid[0].size(); j++)
			{
				if (i - 2 < 0 || obstacleGrid[i - 2][j - 1] != 1)
					res[i][j] += res[i - 1][j];
				if (j - 2 < 0 || obstacleGrid[i - 1][j - 2] != 1)
					res[i][j] += res[i][j - 1];
			}
		}
		return res[obstacleGrid.size()][obstacleGrid[0].size()];
	}
};