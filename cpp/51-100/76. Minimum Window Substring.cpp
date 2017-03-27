class Solution {
public:
	string minWindow(string s, string t) {
		if (s.empty())
			return "";
		if (t.empty())
			return "";
		int low, high, count;
		count = low = 0;
		map<char, int> dict;
		for (int i = 0; i < t.size(); i++)
			dict[t[i]]++;
		int dict_size = dict.size();
		string res = "";
		map<char, int> temp;
		int start, end;
		start = 0;
		end = INT_MAX;
		for (int high = 0; high < s.size(); high++)
		{
			if (dict[s[high]] != NULL)
			{
				temp[s[high]]++;
				if (temp[s[high]] == dict[s[high]])
					count++;
			}
			while (count == dict_size)
			{
				if (end == INT_MAX)
				{
					start = low;
					end = high;
				}
				char t = s[low++];
				if (dict[t] != NULL) {
					temp[t]--;
					if (temp[t] < dict[t])
						count--;
					else {
						if (high - low + 1 < end - start + 1)
						{
							start = low;
							end = high;
						}
					}
				}
				else {
					string temp = s.substr(low, high - low + 1);
					if (high - low + 1 < end - start + 1)
					{
						start = low;
						end = high;
					}
				}
			}
		}
		return end == INT_MAX ? "" : s.substr(start, end - start + 1);
	}
};