class Solution {
private:
    vector<vector<int>> res;
    vector<int> nums;
    int n;
    int k;
public:
    void dfs(int idx, vector<int> &path, int sum, int level){
        if(sum > n || level > k)
            return;
        if(level == k && sum == n){
            res.push_back(path);
            return;
        }
        for(int i = idx; i < 9; i++){
            path.push_back(nums[i]);
            dfs(i + 1, path, sum + nums[i], level + 1);
            path.pop_back();
        }

    }
    vector<vector<int>> combinationSum3(int k, int n) {      
        this->n = n;
        this->k = k;
        nums = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        vector<int> path;
        dfs(0, path, 0, 0);
        return res;
    }
};