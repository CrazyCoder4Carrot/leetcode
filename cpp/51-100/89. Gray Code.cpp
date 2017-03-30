class Solution {
public:
	vector<int> grayCode(int n) {
		vector<int> res;
		res.push_back(0);
		int inc = 1;
		for(int i = 1; i <= n; i++)
		{
			int count = res.size() - 1;
			for(int j = count; j>=0; j--)
			{
				res.push_back(res[j] + inc);
			}
			inc << 1;
		}
		return res;
	}
};