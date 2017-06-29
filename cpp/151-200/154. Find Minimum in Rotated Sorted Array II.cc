class Solution {
public:
    int findMin(vector<int>& nums) {
    	if(nums.empty())
    		return 0;
    	int start = 0, end = nums.size() - 1;
    	while(start < end){
    		int mid = (start + end ) / 2;
    		if(nums[mid] > nums[end])
    			start = mid + 1;
    		else if(nums[mid] < nums[end])
    			end = mid;
    		else
    			end--;
    	}
    	return nums[start];
    }
};