class Solution {
public:
	int numDecodings(string s) {
		std::vector<int> v(s.size() + 1, 0);
		v[0] = 1;
		if (s.size() == 0)
			return 0;
		if (s[0] != '0')
			v[1] = 1;
		else
			v[1] = 0;
		if (s.size() == 1)
			return v[1];
		for (int i = 2; i <= s.size(); i++)
		{
			string temp = s.substr(i - 2, 2);
			if (s[i-1] == '0') {
				if (temp <= "26" && temp >= "10")
					v[i] = v[i - 2];
				else
					v[i] = 0;
			}
			else {
				if (temp <= "26" && temp >= "10")
				{
					v[i] = v[i - 1] + v[i - 2];
				}
				else
					v[i] = v[i - 1];
			}
		}
		return v[s.size()];
	}
};