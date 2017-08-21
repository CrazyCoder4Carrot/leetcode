class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> strs;
        for(auto num : nums){
        	strs.push_back(to_string(num));
        }
        string res = "";
        sort(strs.begin(), strs.end(), [](string &s1, string &s2){return s1 + s2 > s2 + s1;});
        for(auto s: strs){
        	res += s;
        }
        while(res[0] == '0' && res.size() > 1)
        	res.erase(0, 1);
        return res;
    }
};