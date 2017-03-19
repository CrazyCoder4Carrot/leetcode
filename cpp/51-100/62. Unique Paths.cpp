class Solution {
public:
	int uniquePaths(int m, int n) {
		if(m > n)
			return uniquePaths(n, m);
		vector<int> pre(m + 1, 1);
		vector<int> cur(m + 1, 0);
		pre[0] = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = 1; j <= m; j++)
			{
				cur[j] = cur[j-1] + pre[j];
			}
			swap(cur, pre);
		}
		return cur[m];
	}
};