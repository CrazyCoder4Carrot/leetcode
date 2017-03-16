class Solution {
public:
	vector<vector<int>> permuteUnique(vector<int>& nums)
	{
		vector<vector<int>> res;
		sort(nums.begin(), nums.end());
		dfs(0, nums, res);
		return res;
	}
	void dfs(int pos, vector<int> &nums, vector<vector<int>> &res)
	{
		if (pos == nums.size() - 1) {
			res.push_back(nums);
			return;
		}
		for (int i = pos; i < nums.size(); i++)
		{
			if (i != pos && nums[i] == nums[pos])
				continue;
			swap(nums[i], nums[pos]);
			dfs(pos + 1, nums, res);
			swap(nums[i], nums[pos]);
		}
	}
};