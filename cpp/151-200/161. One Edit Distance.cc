#include <iostream>
#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int m = s.size();
        int n = t.size();
        if (m > n)
            return isOneEditDistance(t, s);
        if (n - m > 1)
            return false;
        bool mismatch = false;
        for (int i = 0; i < m; i++) {
            if (s[i] != t[i]) {
                mismatch = true;
                if (m == n)
                    s[i] = t[i];
                else
                    s.insert(i, 1, t[i]);
                break;
            }
        }
        return (!mismatch && n - m == 1) || (mismatch && s == t);
    }
};
