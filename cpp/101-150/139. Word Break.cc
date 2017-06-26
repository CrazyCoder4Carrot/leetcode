class Solution {
private:
	bool flag = false;
public:
    bool wordBreak(string s, vector<string>& wordDict) {
    	if(s.empty())
    		return false;
    	map<string ,bool> dict;
    	for(auto word : wordDict)
    		dict[word] = true;
    	vector<bool> dp(s.size() + 1, false);
    	dp[0] = true;
    	for(int i = 1; i <= s.size(); i++){
    		for(int j = 0; j < i; j++){
    			if(dict.find(s.substr(j, i- j)) != dict.end() && dp[j]){
    				dp[i] = true;
    			}
    		}
    	}
    	return dp[s.size()];
    }
};