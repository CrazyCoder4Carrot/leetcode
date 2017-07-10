class Solution {
public:
	string constructStr(long counter, long upper) {
		if (counter == upper - 1)
			return to_string(counter);
		else
			return to_string(counter) + "->" + to_string(upper - 1);
	}
	vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
		vector<string> res;
		int length = nums.size();
		long prev = (long)lower;
		long cur;
		for (int i = 0; i <= length; i++) {
			if (i == length)
				cur = (long) upper + 1;
			else
				cur = (long) nums[i];
			if (prev < cur) {
				res.push_back(constructStr(prev, cur));
			}
			prev = cur + 1;
		}
		return res;
	}
};