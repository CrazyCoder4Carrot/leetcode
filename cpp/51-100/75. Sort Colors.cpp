class Solution {
public:
	void sortColors(vector<int>& nums) {
		int j = 0, k = nums.size() - 1;
		for (int i = 0; i <= k; i++) {
			if (nums[i] == 0)
			{
				swap(nums[j++], nums[i]);
			}
			if (nums[i] == 2)
			{
				swap(nums[k--], nums[i--]);
			}
		}
	}
};