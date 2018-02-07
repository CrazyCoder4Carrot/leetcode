#include<iostream>
#include<string>
#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
private:
    vector<string> symbols;
    int count;
    string low, high;
public:
    Solution() {
        symbols = {"00", "11", "69", "88", "96"};
        count = 0;
    }
    void dfs(int left, int right, string s) {
        if (left > right) {

            if (s[0] == '0' && s.size() != 1)
                return;
            if (s.size() == low.size() && s < low)
                return;
            if (s.size() == high.size() && s > high)
                return;
            count++;
            return;
        }
        for (int i = 0; i < symbols.size(); i++) {
            s[left] = symbols[i][0];
            s[right] = symbols[i][1];
            if (left == right && symbols[i][0] != symbols[i][1])
                continue;
            dfs(left + 1, right - 1,  s);
        }
    }
    int strobogrammaticInRange(string low, string high) {
        this->low = low;
        this->high = high;
        for (int i = low.size(); i <= high.size(); i++) {
            string s(i, '0');
            dfs(0, i - 1, s);
        }
        return count;
    }
};

int main() {
    auto sol = Solution();
    string low = "50";
    string high = "100";
    cout << sol.strobogrammaticInRange(low, high) << endl;
    return 0;
}