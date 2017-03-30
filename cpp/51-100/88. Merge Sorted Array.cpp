class Solution {
public:
	void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		int index = m + n - 1;
		while (index >= 0 && m >= 1 && n >= 1)
		{
			if (nums1[m - 1] > nums2[n - 1])
			{
				nums1[index] = nums1[--m];
			}
			else {
				nums1[index] = nums2[--n];
			}
			index--;
		}
		while(m >= 1)
			nums1[index--] = nums1[--m];
		while(n >= 1)
			nums1[index--] = nums2[--n];
	}
};