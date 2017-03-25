class Solution {
public:
	bool isNumber(string s) {
		int i = 0;
		while (s[0] == ' ')
			s.erase(0, 1);
		while (s[s.size() - 1] == ' ')
			s.erase(s.size() - 1, 1);
		if (s.empty())
			return false;
		int n_num = 0, n_dot = 0;
		if (s[i] == '-' || s[i] == '+')
			i++;
		for (; (s[i] >= '0' && s[i] <= '9') || s[i] == '.' ; i++) {
			s[i] == '.' ? n_dot++ : n_num++;
		}
		if (n_num < 1 || n_dot > 1)
			return false;
		if (s[i] == 'e') {
			i++;
			if (s[i] == '-' || s[i] == '+')
				i++;
			n_num = 0;
			for (; s[i] <= '9' && s[i] >= '0'; i++, n_num++) {}
			if (n_num < 1)
				return false;
			}
		return s[i] == 0;
	}
};