class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size(), num = 2;
        if (n <= 1)
            return 0;
        vector<vector<int> > dp(num + 1, vector<int>(n, 0));
        for (int k = 1; k <= num; k++) {
            int temp = dp[k - 1][0] - prices[0];
            for (int i = 1; i < n; i++) {
                dp[k][i] = max(dp[k][i - 1], prices[i] + temp);
                temp = max(temp, dp[k - 1][i] - prices[i]);
            }
        }
        return dp[num][n - 1];
    }
};