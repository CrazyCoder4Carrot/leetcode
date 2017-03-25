class Solution {
public:
	int climbStairs(int n) {
		if(n == 0)
			return 0;
		if(n == 1)
			return 1;
		if(n == 2)
			return 2;
		int pre = 1, cur = 2;
		for(int i = 3; i <= n; i++)
		{
			int temp = cur;
			cur = cur + pre;
			pre = temp;
		}
		return cur;
	}
};