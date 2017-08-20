class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res = 0;
        int count = 0;
        for (auto num : nums) {
            if (!count) {
                res = num;
                count++;
            }
            else
                count += (num == res) ? 1 : -1;
        }
        return res;
    }
};