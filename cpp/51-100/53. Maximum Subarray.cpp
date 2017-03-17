class Solution {
public:
	int maxSubArray(vector<int>& nums) {
		int res = 0;
		if (nums.empty())
			return res;
		res = nums[0];
		int maxsum = res;
		int n = nums.size();
		for (int i = 1; i < n; i++) {

			if (res < 0)
				res = nums[i];
			else
			{

				res += nums[i];
			}
			maxsum = max(res, maxsum);
		}
		return maxsum;
	}
};