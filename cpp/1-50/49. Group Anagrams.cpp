class Solution {
public:
	vector<vector<string>> groupAnagrams(vector<string>& strs) {
		vector<vector<string>> res;
		map<string, vector<string>> dict;
		for(auto str: strs){
			string temp = strsort(str);
			dict[temp].push_back(str);
		}
		for(auto it: dict){
			res.push_back(it.second);
		}
		return res;
	}
	string strsort(string s)
	{
		int n = s.size();
		string res(n, 'a') ;
		int a[26] = {0};
		for(int i = 0; i < n; i++)
			a[s[i] - 'a']++;
		int p = 0;
		for(int i = 0; i < 26; i++){
			for(int j = 0; j < a[i]; j++)
				res[p++] += i;
		}
		return res;
	}
};