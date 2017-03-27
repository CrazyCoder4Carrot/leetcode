class Solution {
public:
	vector<vector<int>> subsets(vector<int>& nums) {
		vector<vector<int>> res;
		vector<int> path;
		if (nums.empty())
			return res;
		dfs(0, 0, path, res, nums);
		return res;
	}
	void dfs(int depth, int k, vector<int> &path, vector<vector<int>> &res, vector<int> nums) {
			res.push_back(path);
		for (int i = k; i < nums.size(); i++)
		{
			path.push_back(nums[i]);
			dfs(depth, i + 1, path, res, nums);
			path.pop_back();
		}
	}
};