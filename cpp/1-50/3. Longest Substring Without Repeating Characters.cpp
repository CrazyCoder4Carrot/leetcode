class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> flags(256, -1);
        if(s.empty())
            return 0;
        int res = 1;
        int start = -1;
        for(int i = 0; i < s.size(); i++){
            if(flags[s[i]] > start){
                start = flags[s[i]];
            }
            res = max(res, i - start);
            flags[s[i]] = i;
        }
        return res;
    }
};