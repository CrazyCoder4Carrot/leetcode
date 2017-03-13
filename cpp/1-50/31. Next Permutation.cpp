class Solution {
public:
	void nextPermutation(vector<int>& nums) {
		if (nums.empty())
			return;
		int i = nums.size() - 2;
		for (; i >= 0; i--) {
			if (nums[i] < nums[i + 1])
				break;
		}
		if (i == -1) {
			sort(nums.begin(), nums.end());
			return;
		}
		int j = nums.size() - 1;
		for(;j >= i; j--)
		{
			if(nums[j] > nums[i])
				break;
		}
		swap(nums[i], nums[j]);
		reverse(nums.begin() + i + 1, nums.end());
	}
};