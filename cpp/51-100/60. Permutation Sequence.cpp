class Solution {
public:
	string getPermutation(int n, int k) {
		string s = "";
		k --;
		int count = 1;
		for (int i = 1; i <= n; i++) {
			s += to_string(i);
			count *= i;
		}
		int m = n;
		count /= (m--);
		for (int i = 0; i < n - 1; i++)
		{
			int index = k / count;
			k = k % count;
			swap(s[i], s[i + index]);
			sort(s.begin() + i + 1, s.end());
			count /= (m--);
		}
		return s;
	}
};