#include <iostream>
#include <vector>
#include <math.h>
#include <climits>
using namespace std;
class Solution
{
public:
        int reverse(int x)
        {
                int flag = 1;
                if (x < 0) {
                        flag = -1;
                        x = -x;
                }
                long res = 0;
                while (x)
                {
                        res = res * 10 + x % 10;
                        x /= 10;
                }
                res *= flag;
                return (res > INT_MAX || res < INT_MIN) ? 0 : res;
        }
};

int main()
{
        Solution sol;
        cout << sol.reverse(100) << endl;
}