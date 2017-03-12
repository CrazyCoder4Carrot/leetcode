class Solution {
public:
	vector<int> findSubstring(string s, vector<string>& words) {
		vector<int> res;
		map<string, bool> dict;
		if (words.empty())
			return res;
		int word_size = words[0].size();
		int length = words.size();
		if (s.size() < word_size * words.size())
			return res;
		for (int i = 0; i < words.size(); i++)
		{
			dict[words[i]]++;
		}
		for (int i = 0; i < s.size() - word_size * length + 1; i++)
		{
			map<string, int> cur;
			int j = 0;
			for (;j < length; j++) {
				string temp = s.substr(i + j * word_size, word_size);
				if (dict[temp]) {
					cur[temp]++;
					if (cur[temp] > dict[temp])
						break;
				}
				else break;
			}
			if(j == length)
				res.push_back(i);
		}
		return res;
	}
};
