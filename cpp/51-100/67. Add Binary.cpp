class Solution {
public:
	string addBinary(string a, string b) {
		if (a.empty())
			return b;
		if (b.empty())
			return a;
		int carry = 0;
		int i = a.size() - 1;
		int j = b.size() - 1;
		string res = "";
		while (carry || i >= 0 || j >= 0)
		{
			int temp = carry;
			if (i >=0){
				temp += a[i] - '0';
				i--;
			}
			if (j >= 0){
				temp += b[j] - '0';
				j--;
			}
			carry = temp / 2;
			res = to_string(temp % 2) + res;
		}
		return res;
	}
};