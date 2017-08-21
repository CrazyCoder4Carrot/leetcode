#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
using namespace std;
class Solution {
public:
    string fractionToDecimal(long long n, long long d) {
        if (n == 0)
            return "0";
        string res;
        if (n < 0 ^ d < 0)
            res += '-';
        n = abs(n);
        d = abs(d);
        res += to_string(n / d);
        if (n % d == 0)
            return res;
        res += ".";
        unordered_map<int, int> map;
        for (long long r = n % d; r; r %= d) {
            if (map.count(r) > 0) {
                res.insert(map[r], 1, '(');
                res += ")";
                break;
            }
            map[r] = res.size();
            r *= 10;
            res += to_string(r / d);
        }
        return res;
    }
};

int main()
{
    Solution sol = Solution();
    cout << sol.fractionToDecimal(1, 3) << endl;
}