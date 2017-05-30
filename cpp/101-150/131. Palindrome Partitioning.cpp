class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        if(s.empty())
            return res;
        vector<string> path;
        helper(0, res, s, path);
        return res;
    }
    bool isPanlindrom(string s, int i, int j) {
        while (i <= j) {
            if (s[i++] != s[j--])
                return false;
        }
        return true;
    }
    void helper(int index, vector<vector<string>> &res, string s, vector<string> &path) {
        if(index == s.size())
            res.push_back(path);
        for (int i = index; i < s.size(); i++) {
            if(isPanlindrom(s, index, i)){
                path.push_back(s.substr(index, i - index + 1));
                helper(i + 1, res, s, path);
                path.pop_back();
            }
        }
    }
};