class Solution {
public:
	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		vector<vector<int>> res;
		if(candidates.empty())
			return res;
		vector<int> path;
		helper(candidates, 0, target, path, res, -1);
		return res;
	}
	void helper(vector<int> &candidates, int sum, int target, vector<int> &path, vector<vector<int>> &res, int index)
	{
		if (sum > target)
			return;
		if (sum == target)
		{
			res.push_back(path);
			return;
		}
		for(int i = 0; i < candidates.size(); i++)
		{
		    if(index >=0 && path[index] > candidates[i])
		        continue;
			path.push_back(candidates[i]);
			helper(candidates, sum + candidates[i], target, path, res, path.size() - 1);
			path.pop_back();
		}
	}
};