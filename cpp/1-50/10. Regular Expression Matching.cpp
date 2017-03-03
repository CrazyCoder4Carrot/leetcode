class Solution 
{
public:
    bool isMatch(string s, string p) 
    {
        vector<vector<bool> > table(s.length() + 1, vector<bool>(p.length() + 1));
        table[0][0] = true;
        for(int j = 1; j <= p.length(); j++)
        {
                if(p[j-1] == '*')
                        table[0][j] = table[0][j-2];
        }
        for(int i = 1; i <= s.length(); i++)
        {
                for(int j = 1; j <= p.length(); j++)
                {
                        if(s[i-1] == p[j-1] || p[j-1] == '.')
                                table[i][j] = table[i-1][j-1];
                        if(p[j-1] == '*')
                                table[i][j] = table[i][j-2] | (table[i-1][j] & (p[j-2] == s[i-1]| p[j-2] == '.'));
                }
        }
        return table[s.length()][p.length()];
    }
};