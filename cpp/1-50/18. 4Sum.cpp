class Solution
{
public:
    vector<vector<int> > fourSum(vector<int>& nums, int target)
    {
        vector<vector<int> > res;
        sort(nums.begin(), nums.end());
        if(nums.size() < 4)
            return res;
        for(int i = 0; i < nums.size() - 3;)
        {
            for(int j = i+1; j < nums.size() - 2;)
            {
                int low = j + 1;
                int high = nums.size() - 1;
                while(low < high)
                {
                    int temp = nums[i] + nums[j] + nums[low] + nums[high];
                    if(temp == target){
                        vector<int> temp({nums[i], nums[j], nums[low], nums[high]});
                        res.push_back(temp);
                        do{
                            low++;
                        }while(low < high && nums[low] == nums[low-1]);
                        do{
                            high--;
                        }while(low < high && nums[high] == nums[high + 1]);
                    }
                    if(temp < target)
                    {
                        do{
                            low++;
                        }while(low < high && nums[low] == nums[low-1]);

                    }
                    if(temp > target)
                    {
                        do{
                            high--;
                        }while(low < high && nums[high] == nums[high + 1]);
                    }
                }
                do{
                    j++;
                }while(j < nums.size() - 2 && nums[j] == nums[j-1]);
            }
            do{
                i++;
            }while(i < nums.size() - 3 && nums[i] == nums[i-1]);
        }
        return res;
    }
};