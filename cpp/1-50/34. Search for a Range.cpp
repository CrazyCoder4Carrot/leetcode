class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) 
    {
        vector<int> res(2, -1);
        if(nums.empty())
            return res;
        res[0] = serachLeft(nums, target);
        res[1] = serachRight(nums, target);
        return res;
    }
    int serachLeft(vector<int>& nums, int target)
    {
        int low = 0, high = nums.size() - 1;
        while(low <= high)
        {
            int mid = (low + high) / 2;
            if(nums[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return nums[low] == target ? low: -1;
    }
    int serachRight(vector<int>& nums, int target)
    {
        int low = 0, high = nums.size() - 1;
        while(low <= high){
            int mid = (low + high) / 2;
            if(nums[mid] > target)
                high = mid - 1;
            else
                low = mid + 1;
        }
        return nums[high] == target? high: -1;
    }
};