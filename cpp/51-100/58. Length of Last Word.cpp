class Solution {
public:
	int lengthOfLastWord(string s) {
		if(s.empty())
			return 0;
		int count = 0;
		int start = s.size() - 1;
		while(s[start] == ' ')
			start --;
		for (int i = start ; i >= 0; i--)
		{
			if(s[i] == ' ')
				break;
			count++;
		}
		return count;
	}
};