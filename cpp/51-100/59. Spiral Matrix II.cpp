#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
	vector<vector<int> > generateMatrix(int n) {
		vector<int> row;
		row.push_back(n*n);
		vector<vector<int> > matrix;
		if (n == 0)
			return matrix;
		matrix.push_back(row);
		n = n*n - 1;
		while (n > 0)
		{
			vector<int> row;
			while (n >= matrix[0][matrix[0].size() - 1] - matrix[0].size()) {
				cout << n << endl;
				row.push_back(n);
				n--;
			}
			reverse(row.begin(), row.end());
			if (!row.empty())
			{
				matrix.insert(matrix.begin(), row);
				if( n > 0)
				    matrix = rotate(matrix);
			}

		}
		return matrix;
	}
	vector<vector<int>> rotate(vector<vector<int>> &matrix) {
		vector<vector<int>> temp;
		for (int i = 0; i < matrix[0].size(); i++)
		{
			vector<int> row;
			for (int j = matrix.size() - 1; j >= 0 ; j--)
			{
				row.push_back(matrix[j][i]);
			}
			temp.push_back(row);
		}
		return temp;
	}
};
