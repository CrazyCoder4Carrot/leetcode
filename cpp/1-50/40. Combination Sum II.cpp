class Solution {
public:
	vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
		vector<vector<int>> res;
		if (candidates.empty())
			return res;
		sort(candidates.begin(), candidates.end());
		vector<int> path;
		helper(0, target, path, candidates, res);
		return res;
	}
	void helper(int index, int sub, vector<int> &path, vector<int> &candidates, vector<vector<int>> &res)
	{
		if (sub < 0 || index > candidates.size())
			return;
		if (sub == 0) {
			res.push_back(path);
			return;
		}
		for (int i = index; i < candidates.size(); i++) {
			while (i > index && candidates[i] == candidates[i - 1])
				i++;
			path.push_back(candidates[i]);
			helper(i + 1, sub - candidates[i], path, candidates, res);
			path.pop_back();
		}
	}
};