class Solution {
public:
	int divide(long dividend, long divisor) {
		int flag = false;
		if (dividend < INT_MIN || dividend > INT_MAX)
			return INT_MAX;
		if (divisor < INT_MIN || divisor > INT_MAX)
			return INT_MAX;
		if (dividend < 0){
			flag = !flag;
			dividend = -dividend;
		}
		if (divisor < 0){
			flag = !flag;
			divisor = -divisor;
		}
		if(dividend < divisor)
			return 0;
		long res = 0;
		while(dividend > 0 || dividend >= divisor){
			long temp = 1;
			long div = divisor;
			while(div < dividend){
				div <<= 1;
				temp <<= 1;
			}
			if(div > dividend)
			{
				div >>= 1;
				temp>>= 1;
			}
			dividend -= div;
			res += temp;
		}
		res = flag? -res: res;
		if(res < INT_MIN || res > INT_MAX){
			return INT_MAX;
		}
		else
			return res;
	}
};