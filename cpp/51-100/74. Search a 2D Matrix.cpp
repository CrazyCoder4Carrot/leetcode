class Solution {
public:
	bool searchMatrix(vector<vector<int>>& matrix, int target) {
		if(matrix.empty())
			return false;
		int m = matrix.size(), n = matrix[0].size();
		if(m == 0 || n == 0)
			return false;
		int low = 0, high = m - 1;
		if(target < matrix[0][0] || target > matrix[m-1][n-1])
			return false;
		int mid;
		while(low <= high)
		{
			mid = (low + high) / 2;
			if(matrix[mid][0] <= target && matrix[mid][n-1] >= target)
				break;
			if(matrix[mid][0] > target)
				high = mid - 1;
			else if(matrix[mid][n-1] < target)
				low = mid + 1;
		}
		int i = mid;
		low = 0, high = n - 1;
		while(low <= high)
		{
			int mid = (low + high) / 2;
			if(matrix[i][mid] == target)
				return true;
			else if(matrix[i][mid] < target)
				low = mid + 1;
			else
				high = mid - 1;
		}
		return false;
	}
};