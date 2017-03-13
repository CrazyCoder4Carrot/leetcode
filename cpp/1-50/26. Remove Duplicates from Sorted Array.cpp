#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
	int removeDuplicates(vector<int>& nums) {
		if (nums.empty())
			return 0;
		int slow = 0;
		int key = nums[0];
		for (int i = 1; i < nums.size(); i++)
		{
			if (key < nums[i])
			{
				key = nums[i];
				slow++;
				nums[slow] = nums[i];
			}
			else
			{
				if (key > nums[i])
					break;
			}
		}
		return slow + 1;
	}
};