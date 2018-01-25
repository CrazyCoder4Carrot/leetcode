class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty())
            return 0;
        if (nums.size() == 1)
            return nums[0];
        int prev = 0, cur = 0, res = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            auto tmp = cur;
            cur = max(cur, prev + nums[i]);
            prev = tmp;
        }
        res = cur;
        prev = 0, cur = 0;
        for(int i = 1; i < nums.size(); i++){
            auto tmp = cur;
            cur = max(cur, prev + nums[i]);
            prev = tmp;
        }
        return max(res, cur);
    }
};