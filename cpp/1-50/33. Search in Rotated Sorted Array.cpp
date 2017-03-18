class Solution {
public:
	int search(vector<int>& nums, int target) {
		int low = 0;
		int high = nums.size() - 1;
		while(low <= high)
		{
			int mid = (low + high) / 2;
			int num = (target < nums[0]) == (nums[mid] < nums[0])?
						nums[mid]: target < nums[0]? INT_MIN:INT_MAX;
			if(num < target)
				low = mid + 1;
			else if(num > target)
				high = mid - 1;
			else
			    return mid;
		}
		return -1;
	}
};