class Solution {
public:
	vector<int> plusOne(vector<int>& digits) {
		int carry = 1;
		for(int i = digits.size() - 1;i>=0 && carry ;i--)
		{
		    int temp = digits[i] + carry;
			carry = temp / 10;
			digits[i] = temp % 10;
		}
		if(carry)
			digits.insert(digits.begin(), carry);
		return digits;
	}
};