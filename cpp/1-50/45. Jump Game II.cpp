class Solution {
public:
	int jump(vector<int>& nums) {
		if (nums.empty())
			return 0;
		int curmax = nums[0], maxpos = nums[0], jumpcnt = 1;
		int size = nums.size();
		for (int i = 1; i <= min(size - 1, maxpos); i++)
		{
			if (i == size - 1)
				return jumpcnt;
			curmax = max(curmax, nums[i] + i);
			if (i == maxpos) {
				maxpos = curmax;
				jumpcnt++;
			}
		}
		return 0;
	}
};