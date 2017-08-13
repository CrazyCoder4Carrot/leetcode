class Solution {
private:
    int minmove = INT_MAX;
    bool validMove(string s1, string s2) {
        int count = 0;
        if (s1.size() != s2.size())
            return false;
        for (int i = 0; i < s1.size(); i++) {
            if (s1[i] != s2[i])
                count++;
        }
        return count == 1;
    }
public:

    int minMutation(string start, string end, vector<string>& bank) {
        dfs(0, start, end, 0, bank);
        if (minmove == INT_MAX)
            return -1;
        else
            return minmove;
    }
    void dfs(int index, string cur, string end, int mvCnt, vector<string> &bank) {
        if (cur == end) {
            minmove = min(minmove, mvCnt);
            return ;
        }
        for (int i = index; i < bank.size(); i++) {
            if (validMove(cur, bank[i])) {
                swap(bank[i], bank[index]);
                dfs(index + 1, bank[index], end, mvCnt + 1, bank);
                swap(bank[i], bank[index]);
            }
        }
    }
};