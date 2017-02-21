#include <algorithm>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> pair;
        vector<int> res;
        for(int i = 0; i < nums.size(); i++)
        {
            int temp = target - nums[i];
            if(pair.find(temp) != pair.end())
            {
                res.push_back(pair[temp]);
                res.push_back(i);
                return res;
            }
            pair[nums[i]] = i;
        }
    }
};