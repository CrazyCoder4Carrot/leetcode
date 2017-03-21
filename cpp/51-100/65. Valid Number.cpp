class Solution {
public:
	bool isNumber(string s) {
		int i = 0;
		while (s[i] == ' ')
			s.erase(0, 1);
		
		while (s[s.size() - 1] == ' ')
			s.erase(s.size() - 1, 1);
		if (s.empty())
			return false;
		if (s[i] == '+' || s[i] == '-')
			i++;
		int n_number = 0, n_dot = 0;
		for (; ((s[i] <= '9' && s[i] >= '0') || s[i] == '.'); i++)
			s[i] == '.' ? n_dot++ : n_number++;
		if (n_dot > 1 || n_number < 1)
			return false;
		if (s[i] == 'e') {
			i++;
			if (s[i] == '+' || s[i] == '-' ) i++;
			n_number = 0;
			for (; s[i] <= '9' && s[i] >= '0'; i++, n_number++){}
			if (n_number < 1)
				return false;
		}
		return s[i] == 0;
	}
};