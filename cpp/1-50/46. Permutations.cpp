class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        helper(0, nums, res);
        return res;
    }
    void helper(int pos, vector<int> &nums, vector<vector<int>> &res)
    {
    	if(pos == nums.size())
    	{
    		res.push_back(nums);
    		return;
    	}
    	for(int i = 0; i < nums.size(); i++)
    	{
    		swap(nums[i], nums[pos]);
    		helper(nums, res);
    		swap(nums[pos], nums[i]);
    	}
    }
};