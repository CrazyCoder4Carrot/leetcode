class Solution {
public:
	vector<int> spiralOrder(vector<vector<int>>& matrix) {
		vector<int> res;
		while (!matrix.empty()) {
			res.insert(res.end(), matrix[0].begin(), matrix[0].end());
			vector<vector<int>> new_matrix;
			for (int j = matrix[0].size() - 1; j >= 0 ; j--)
			{
				vector<int> row;
				for (int i = 1; i < matrix.size(); i++)
				{
					row.push_back(matrix[i][j]);
				}
				new_matrix.push_back(row);
			}
			matrix = new_matrix;
		}
		return res;
	}
};