class Solution {
public:
	bool isInterleave(string s1, string s2, string s3) {
		if(s3.size() != (s1.size() + s2.size()))
			return false;
		map<char, int> dict;
		for(int i = 0; i < s1.size(); i++)
			dict[s1[i]]++;
		for(int i = 0; i < s2.size(); i++)
			dict[s2[i]]++;
		for(int i = 0; i < s3.size(); i++)
			dict[s3[i]]--;
		for(int i = 0; i < 26; i++)
			if(dict[i + 'a'])
				return false;
		return helper(s1, s2, s3, 0, 0, 0);
	}
	bool helper(string s1, string s2, string s3, int index1, int index2, int index3){
		if(index1 >= s1.size() && index2 >= s2.size() && index3 >= s3.size())
			return true;
		if(s1[index1] != s3[index3] && s2[index2] != s3[index3])
			return false;
		bool res = false;
		int t1 = index1;
		int t3 = index3;
		while(s1[t1++] == s3[t3++]){
			res |= helper(s1, s2, s3, t1, index2, t3);
		}
		int t2 = index2;
		t3 = index3;
		while(s2[t2++] == s3[t3++])
			res |= helper(s1, s2, s3, index1, t2, t3);
		return res;
	}
};