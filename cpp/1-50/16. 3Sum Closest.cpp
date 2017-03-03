#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
class Solution
{
public:
    int threeSumClosest(vector<int>& nums, int target)
    {
        sort(nums.begin(), nums.end());
        if(nums.size() < 3)
            return -1;
        int res = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.size() - 2; i++)
        {
            int low = i + 1;
            int high = nums.size() - 1;
            while (low < high) {
                int temp = nums[i] + nums[low] + nums[high];
                if (abs(temp - target) < abs(res - target))
                    res = temp;
                if (temp < target)
                    low++;
                if (temp > target)
                    high--;
                if(temp == target)
                    return temp;
            }
        }
        return res;
    }
};
