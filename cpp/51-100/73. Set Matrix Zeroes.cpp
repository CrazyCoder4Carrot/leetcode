class Solution {
public:
	void setZeroes(vector<vector<int>>& matrix)
	{
		bool row = false, col = false;
		for (int j = 1; j < matrix[0].size(); j++)
			if (matrix[0][j] == 0)
				row = true;
		for (int i = 1; i < matrix.size(); i++)
			if (matrix[i][0] == 0)
				col = true;
		for (int i = 1; i < matrix.size(); i++) {
			for (int j = 1; j < matrix[0].size(); j++)
				if (matrix[i][j] == 0) {
					matrix[0][j] = matrix[i][0] = 0;
				}
		}
		for (int i = 1; i < matrix.size(); i++) {
			if (matrix[i][0] == 0) {
				vector<int> temp(matrix[0].size(), 0);
				matrix[i] = temp;
			}
		}
		for (int j = 1; j < matrix[0].size(); j++) {
			if (matrix[0][j] == 0)
			{
				for (int i = 1; i < matrix.size(); i++)
					matrix[i][j] = 0;
			}
		}
		if (matrix[0][0] == 0)
		{
			vector<int> temp(matrix[0].size(), 0);
			matrix[0] = temp;
			for (int i = 0; i < matrix.size(); i++)
				matrix[i][0] = 0;
		}
		if (row) {
			vector<int> temp(matrix[0].size(), 0);
			matrix[0] = temp;
		}
		if (col)
		{
			for (int i = 0; i < matrix.size(); i++)
				matrix[i][0] = 0;
		}
	}
};