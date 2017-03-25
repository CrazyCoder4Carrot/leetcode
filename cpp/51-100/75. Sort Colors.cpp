class Solution {
public:
	void sortColors(vector<int>& nums) {
		int red = white = blue = 0;
		for (int i = 0; i < nums.size(); i++) {
			if (nums[i] == 0)
				red++;
			if (nums[i] == 1)
				white++;
			if (nums[i] == 2)
				blue++;
		}
		for (int i = 0; i < red; i++)
			nums[i] = 0;
		for (int i = 0; i < white; i++)
			nums[red + i] = 1;
		for (int i = 0; i < blue; i++)
			nums[ white + red + i] = 1;

	}
};