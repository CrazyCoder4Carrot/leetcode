class Solution {
public:
    double myPow(double x, int n) {
        long p = n;
        if(p < 0)
        {
        	x = 1/x;
        	p = -p;
        }
        double res = 1;
        while(p > 0){
        	if(p & 1)
        		res *= x;
        	p  >>= 1;
        	x *= x;
        }
        return res;
    }
};