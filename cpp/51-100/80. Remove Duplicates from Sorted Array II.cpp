class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		int low = 0;
		for (auto n : nums)
			if (low < 2 || n > nums[i - 1])
				nums[i++] = n;
	}
};