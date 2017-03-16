class Solution {
public:
	void rotate(vector<vector<int>>& matrix) {
		int n = matrix.size() - 1;
		for(int i = 0; i <= n / 2; i ++)
		{
			swap(matrix[i][i], matrix[n - i][n - i]);
			swap(matrix[i][n-i], matrix[n-1][i]);
		}
	}
};