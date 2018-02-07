class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> dict;
        for(int i = 0; i < nums.size(); i++){
            if(dict.find(nums[i]) != dict.end() && i - dict[nums[i]] <= k){
                return true;
            }
            else{
                dict[nums[i]] = i;
            }
        }
        return false;
    }
};