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
				res += nums[i];
			maxsum = max(res, maxsum);
		}
		return maxsum;
	}
};

class Solution {
public:
	int maxSubArray(vector<int>& nums) {
		return helper(0, nums.size() - 1, nums);
	}
	int helper(int left, int right, vector<int>& nums) {
		if (left == right)
			return  nums[left];
		int mid = (left + right) / 2;
		int leftval = helper(left, mid, nums);
		int rightval = helper(mid + 1, right, nums);
		int midval = nums[mid] + nums[mid + 1];
		int temp = mid - 1;
		int res = midval;
		while (temp >= left) {
			res += nums[temp];
			midval = max(res, midval);
		}
		temp = mid + 2;
		res = midval;
		while (temp <= right){
			res += nums[temp];
			midval = max(res, midval);
		}
		return max(leftval, rightval, midval);
	}
};