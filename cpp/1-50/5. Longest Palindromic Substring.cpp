#include <string>
#include <iostream>
using namespace std;
class Solution {
public:
	void expand(int start, int end, string s, string &res)
	{
		while (start >= 0 && end < s.length() && s[start] == s[end])
		{
			if ((end - start + 1) > res.length())
				res = s.substr(start, end - start + 1);
			start--;
			end++;
		}
	}
	bool isPalindrome(string s)
	{
		int start = 0, end = s.length();
		while (start <= end && s[start] == s[end])
		{
			start++;
			end--;
		}
		return start == end;
	}
	string longestPalindrome(string s) 
	{
		if (isPalindrome(s))
			return s;
		string res = "";
		res.push_back(s[0]);
		for (int i = 0; i < s.length(); i++)
		{
			if (i - 1 < 0 || i + 1 > s.length())
				continue;
			if (s[i - 1] == s[i + 1]) {
				int start = i - 1, end = i + 1;
				expand(start, end, s, res);
			}
			if (s[i - 1] == s[i]) {
				int start = i - 1, end = i;
				expand(start, end, s, res);
			}

		}
		return res;
	}

};

int main()
{
	Solution sol ;
	string res = sol.longestPalindrome("abbsbbsbs");
	cout<<res<<endl;
}