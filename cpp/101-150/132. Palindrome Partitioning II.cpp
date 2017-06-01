class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> cut(n + 1, 0);
        for (int i = 0; i <= n; i++)
            cut[i] = i - 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; i >= j && i + j < n && s[i - j] == s[i + j]; j++)
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j]);
            for (int j = 0; i - j + 1 >= 0 && i + j < n && s[i - j + 1] == s[i + j]; j++)
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j + 1]);
        }
        return cut[n];
    }
};