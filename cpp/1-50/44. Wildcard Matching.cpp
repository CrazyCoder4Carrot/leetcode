class Solution {
public:
	bool isMatch(string s, string p) {
		return helper(s, p, 0, 0) == 2;
	}
	int helper(string s, string p, int si, int pi)
	{
		if (si == s.size() && pi == p.size())
			return 2;
		if (si == s.size() && p[pi] != '*')
			return 1;
		if (pi == p.size())
			return 0;
		if (p[pi] == '*') {
			while (pi + 1 < p.size() && p[pi] == p[pi + 1]) {pi++;}
			for (int i = 0; i <= s.size() - si; i++)
			{
				int ret = helper(s, p, si + i, pi + 1);
				if (ret == 2 || ret == 1)
					return ret;
			}
		}
		if (p[pi] == s[si] || p[pi] == '?')
			return helper(s, p, si + 1, pi + 1);
		return 0;
	}
};

