#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
class Solution
{
public:
    vector<string> letterCombinations(string digits)
    {
        vector<string> res;
        if(digits.empty() || digits.find('1') != string::npos || digits.find("0") != string::npos)
            return res;
        map<char, string> phone;
        phone['2'] = "abc";
        phone['3'] = "def";
        phone['4'] = "ghi";
        phone['5'] = "jkl";
        phone['6'] = "mno";
        phone['7'] = "pqrs";
        phone['8'] = "tuv";
        phone['9'] = "wxyz";
        helper(digits, "", digits.size(), phone, res);
        return res;
    }
    void helper(string digits, string path, int count, map<char, string> phone, vector<string> &res)
    {
        if(path.size() == count)
        {
            res.push_back(path);
            return;
        }
        string s = phone.find(digits[0])->second;
        for(int i = 0; i < s.size(); i++)
        {
            path.push_back(s[i]);
            helper(digits.substr(1, digits.size() - 1), path,count, phone, res);
            path = path.substr(0, path.size() - 1);
        }
    }
};

int main()
{
    Solution sol;
    vector<string> res;
    res = sol.letterCombinations("2");
}