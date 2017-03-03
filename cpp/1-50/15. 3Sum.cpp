class Solution {
public:
	vector<vector<int>> threeSum(vector<int>& nums) {
		vector<vector<int> > res;
		if (nums.empty())
			return res;
		sort(nums.begin(), nums.end());
		if (nums[0] > 0)
			return res;
		int start = 0;
		while (start < nums.size() && nums[start] <= 0)
		{
			int low = start + 1;
			int high = nums.size() - 1;
			int start_val = nums[start];
			while (low < high)
			{
				int sum = 0;
				vector<int> temp;
				int low_val = nums[low];
				int high_val = nums[high];
				sum = nums[low] + nums[high] + nums[start];
				if (sum == 0)
				{
					temp.push_back({nums[start], nums[low], nums[high]});
					low++;
					high--;
					while (low < high && nums[low] == nums[low - 1]) low++;
					while (low < high && nums[high] == nums[high + 1]) high--;
				}
				else {
					if (sum > 0)
					{
						do {
							high --;
						}
						while (high > low && high_val == nums[high]);
					}
					else {
						do {
							low ++;
						}
						while (high > low && low_val == nums[low]);
					}
				}
			}
			do {
				start++;
			}
			while (start < nums.size() && start_val == nums[start]);
		}
		return res;
	}
};