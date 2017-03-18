class Solution {
public:
	bool canJump(vector<int>& nums) {
		int reach = 0;
		int n = nums.size() - 1;
		int i = 0;
		for(; i <= min(reach, n); i++)
			reach = max(reach, i + nums[i]);
		return i == n + 1;
	}
};