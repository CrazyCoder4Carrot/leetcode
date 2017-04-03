class Solution {
public:
	int numTrees(int n) {
		if(n == 0 || n == 1)
			return 1;
		std::vector<int> dp(n + 1, 0);
		dp[0] = 1;
		for(int i = 2; i < n + 1; i++)
			for(int j = 1; j <= i; j++)
				dp[i] += dp[j-1] * dp[i - j];
		return dp[n];
	}
};