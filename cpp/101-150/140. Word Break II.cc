class Solution {
private:
    unordered_map<string, vector<string>> m;
    unordered_map<string, bool> dict;
    vecotr<string> combine(string word, vector<string> &prev) {
        for (int i = 0 ; i < prev.size(); i++) {
            prev[i] += " " + word;
        }
        return prev;
    }
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
    	for(string word : wordDict){
    		dict[word] = true;
    	}
    	return helper(s, dict);
    }
    vector<string> helper(string s, unordered_map<string, bool> &dict){
    	if(m[s] != m.end())
    		return m[s];
    	vector<string> res;
    	if(dict[s])
    		res.push_back(s);
    	for(int i = 1; i < s.size(); i++){
    		string word = s.substr(i);
    		if(dict[word] != dict.end()){
    			string rem = s.substr(0, i);
    			vector<string> prev = combine(word, helper(rem, dict));
    			res.insert(res.end(), prev.begin(), prev.end());
    		}
    	}
    	m[s] = res;
    	return res;
    }
};