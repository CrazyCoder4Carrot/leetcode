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
        int res = INT_MAX;
        for (int i = 0; i < nums.size() - 2;)
        {
            int low = i + 1;
            int high = nums.size() - 1;
            while (low < high) {
                int temp = nums[i] + nums[low] + nums[high];
                if (abs(temp - target) < abs(res - target))
                    res = temp;
                if (temp < target)
                {
                    do {
                        low++;
                    } while (low < high && nums[low] == nums[low-1]);
                }
                if (temp > target)
                {
                    do{
                        high--;
                    }while( low < high && nums[high] == nums[high + 1]);
                }
                if(temp == target)
                {
                    res = temp;
                    do {
                        low++;
                    } while (low < high && nums[low] == nums[low-1]);
                    do{
                        high--;
                    }while( low < high && nums[high] == nums[high + 1]);
                }
            }
            do{
                i++;
            }while(i < nums.size() - 2 && nums[i] == nums[i-1]);
        }
        return res;
    }
};

int main()
{
    Solution sol;
    std::vector<int> v;
    v.push_back(0);
    v.push_back(2);
    v.push_back(1);
    v.push_back(-3);
    cout<<sol.threeSumClosest(v, 1)<<endl;
}