class Solution {
public:
	int firstMissingPositive(vector<int>& nums) {
		for (int i = 0; i < nums.size(); i++) {
			while (nums[i] > 0 && nums[i] < nums.size() && nums[i] != nums[nums[i] - 1])
			{
				swap(nums[i], nums[nums[i] - 1]);

			}
		}
		int j = 0;
		for (; j < nums.size(); j++)
		{
			if (nums[j] != j + 1)
				break;
		}
		return j + 1;
	}
};