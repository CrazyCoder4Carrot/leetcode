class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty())
            return "";
        if(strs.size() == 1)
            return strs[0];
        bool flag = true;
        int index = 0;
        string res = "";
        for(int i = 0; i < strs[i].size(); i++)
        {
            char c = strs[0][i];
            for(int j = 1; j < strs.size(); j++)
            {
                if(c != strs[j][i])
                    flag = false;
            }
            if(!flag)
            {
                break;
            }
            res.push_back(c);
        }
        return res;
    }
};