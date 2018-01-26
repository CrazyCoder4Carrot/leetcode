class Solution {
public:
    int quickselect(vector<int> nums, int start, int end, int k){
        if(start == end)
            return nums[start];
        int mid = (start + end) / 2;
        int pivot = nums[mid];
        swap(nums[mid], nums[end]);
        int low = start;
        for(int i = start; i < end; i ++){
            if(nums[i] >= pivot){
                swap(nums[low], nums[i]);
                low++;
            }
        }
        swap(nums[low], nums[end]);
        cout<<start<<" "<<end<<" "<<k<<endl;
        int index = low - start;
        if(index == k)
            return pivot;
        else if(k < index)
            return quickselect(nums, start, low - 1, k);
        else
            return quickselect(nums, low + 1, end, k - index - 1);
    }
    int findKthLargest(vector<int>& nums, int k) {
        return quickselect(nums, 0, nums.size() - 1, k - 1);
    }
};