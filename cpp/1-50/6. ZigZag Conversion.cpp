#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) 
    {
        string res = "";
        if(numRows == 1)
                return s;
        int gap = numRows * 2 - 2;
        for(int j = 0; j < s.length(); j += gap)
                res.push_back(s[j]);
        int leftgap = numRows * 2 - 2;
        int rightgap = 0;
        for(int i = 1; i < numRows - 1;i++)
        {                
                leftgap -=2;
                rightgap += 2;
                for(int j = i;j < s.length();)
                {
                        res.push_back(s[j]);
                        j += leftgap;
                        if(j < s.length())
                                res.push_back(s[j]);
                        j += rightgap;
                }
        }
        for(int j = numRows - 1; j < s.length(); j += gap)
                res.push_back(s[j]);
        return res;
    }
};
int main()
{
        string s = "PAYPALISHIRING";
        Solution sol;
        string res = sol.convert(s, 3);
        cout<<res<<endl;
}