class Solution {
public:
	vector<string> restoreIpAddresses(string s) {
		vector<string> path;
		vector<string> res;
		if(s.size() > 16)
			return res;
		dfs(path, s, res);
		return res;
	}
	void dfs(vector<string> path, string s, vector<string> &res) {
		if (s.empty() && path.size() == 4) {
		    stringstream temp;
			for (int i = 0; i < path.size(); i++) {
				if (i != 0)
					temp << ".";
				temp << path[i];
			}
			res.push_back(temp.str());
		}
		int len = s.size();
		int max_len = min(3, len);
		for (int i = 1; i <= max_len; i++) {
			string str_temp = s.substr(0, i);
			if(str_temp.size()>= 2 && str_temp[0] == '0')
				continue;
			if(stoi(str_temp) > 255)
				continue;
			path.push_back(str_temp);
			dfs(path, s.substr(i), res);
			path.pop_back();
		}
	}
};