class Solution {
public:
	int mySqrt(long x) {
		long low = 0, high = x;
		long mid;
		while(low <= high)
		{
			mid = (low + high) / 2;
			if(mid * mid <= x && (mid + 1) * (mid + 1) > x)
				return mid;
			else
				if(mid * mid > x)
					high = mid - 1;
				else
					low = mid + 1;
		}
		return mid;
	}
};