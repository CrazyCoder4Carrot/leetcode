class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        unordered_map<char, int> dict;
        int res = 0, j = -1;
        for (int i = 0; i < s.size(); i++) {
            dict[s[i]]++;
            if (dict.size() <= 2) {
                res = max(res, i - j);
            }
            while (dict.size() > 2) {
                dict[s[++j]] --;
                if (dict[s[j]] == 0)
                    dict.erase(s[j]);
            }
        }
        return res;
    }
};