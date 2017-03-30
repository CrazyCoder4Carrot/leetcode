class Solution {
public:
	bool isScramble(string s1, string s2) {
		if (s1.size() != s2.size())
			return false;
		if(s1 == s2)
			return true;
		map<char, int> dict1;
		map<char, int> dict2;
		for (int i = 0; i < s1.size(); i++) {
			dict1[s1[i]]++;
		}
		for (int i = 0; i < s2.size(); ++i) {
			dict2[s2[i]]++;
		}
		for (int i = 0; i < 26; i++) {
			if (dict1['a' + i] != dict2['a' + i])
				return false;
		}
		for(int i = 1; i < s1.size(); i++)
		{
			if(isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i)))
				return true;
			if(isScramble(s1.substr(0, i), s2.substr(len - i)) && isScramble(s1.substr(i), substr(0, len - i)))
				return true
		}
	}
};