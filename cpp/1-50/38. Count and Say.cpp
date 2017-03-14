class Solution {
public:
	string countAndSay(int n) {
		string s = "1";
		for (int i = 0; i < n - 1; i++) {
			string temp = "";
			for (int j = 0; j < s.size();) {
				int count = 1;
				while(s[j] == s[j+count])
				{
					count++;
				}
				temp += to_string(count) + s[j]; 
				j += count;
			}
			s = temp;
		}
		return s;
	}
};