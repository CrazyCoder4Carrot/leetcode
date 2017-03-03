
class Solution {
public:
	int romanToInt(string s) {
		string romanstr[13] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
		int romanval[13] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
		map <string, int> dict;
		for(int i = 0; i < 13; i++)
			dict[romanstr[i]] = romanval[i];
		int res = 0;
		int pre = 1000, cur;
		for(int i = 0; i < s.size(); i++)
		{
			cur = dict.find(s.substr(i, 1))->second;
			if(pre < cur)
				res += cur - pre * 2;
			else
				res += cur;
			pre = cur;
		}
		return res;
	}
};