class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        if (s.empty() || s.size() <= 10)
            return res;
        unordered_map<string, int> map;
        for (int i = 0; i < s.size() - 9; i++) {
            string tmp = s.substr(i, 10);
            map[tmp] ++;
            if (map[tmp] == 2)
                res.push_back(tmp);
        }
        return res;
    }
};