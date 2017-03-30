class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> path;
        dfs(0, path, nums, res);
        return res;
    }
    void dfs(int k, vector<int> path, vector<int> nums, vector<vector<int>> &res)
    {
    	if(k > nums.size())
    		return;
    	res.push_back(path);
    	for(int i = k; i < nums.size(); i++)
    	{
    		if(i != k && nums[i] == nums[i-1])
    			continue;
    		path.push_back(nums[i]);
    		dfs(i + 1, path, nums, res);
    		path.pop_back();
    	}
    }
};
