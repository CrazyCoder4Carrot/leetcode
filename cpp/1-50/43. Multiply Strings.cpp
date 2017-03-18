class Solution {
public:
	string multiply(string num1, string num2)
	{
		if(num1 == "0" || num2 == "0")
			return "0";
		string res = "";
		for (int i = num2.size() - 1; i >= 0; i--) {
			string temp = mul(num1, num2[i]);
			string zeros(num2.size() - 1 - i, '0');
			if(temp != "0")
				temp = temp + zeros;
			res = add(res, temp);
		}
		return res;
	}
	string mul(string s1, char c)
	{
		string res;
		int carry = 0;
		for (int i = s1.size() - 1; i >= 0 ; i--) {
			int temp = (s1[i] - '0') * (c - '0') + carry;
			res = to_string(temp % 10) + res;
			carry = temp / 10;
		}
		if (carry)
			res = to_string(carry) + res;
		return res;
	}
	string add(string num1, string num2) {
		if (num1.empty())
			return num2;
		if (num2.empty())
			return num1;
		string res = "";
		int minlen = min(num1.size(), num2.size());
		int i = num1.size() - 1, j = num2.size() - 1, carry = 0, temp = 0;
		while (i >= 0 && j >= 0)
		{
			temp = carry + (num1[i] - '0') + (num2[j] - '0');
			res = to_string(temp % 10) + res;
			carry = temp / 10;
			i--;
			j--;
		}
		int k = i >= 0 ? i : j;
		string tempstr = num1.size() < num2.size() ? num2 : num1;
		for (; k >= 0 ; k--)
		{
			temp = carry + (tempstr[k] - '0');
			res = to_string(temp % 10) + res;
			carry = temp / 10;
		}
		if (carry)
		{
			res = to_string(carry) + res;
		}
		return res;
	}
};
