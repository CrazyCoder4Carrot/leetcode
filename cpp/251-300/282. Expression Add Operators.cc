class Solution {
private:
    string op = "+-*";
public:
    vector<string> addOperators(string num, int target) {
        vector<string> res;
        helper(num, 0, target, "", res);
        return res;
    }
    bool cal(string s, int target) {
        long res = 0;
        long cur_res = 0;
        char op = '+';
        for (int i = 0; i < s.size();) {
            if (isdigit(s[i])) {
                long num = 0;
                while (i < s.size() && isdigit(s[i])) {
                    num = num * 10 + s[i] - '0';
                    i++;
                }
                switch (op) {
                case '+':
                    cur_res += num; break;
                case '-':
                    cur_res -= num; break;
                case '*':
                    cur_res *= num; break;
                }
            }
            else {
                if (s[i] == '-' || s[i] == '+') {
                    res += cur_res;
                    cur_res = 0;
                }
                op = s[i++];
            }
        }
        return (res + cur_res) == target;
    }
    void helper(string num, int index, int target, string path, vector<string> &res) {
        if (index == num.size()) {
            if (cal(path, target))
                res.push_back(path);
        }
        for (int i = 1; i + index <= num.size(); i++) {
            if (i >= 2 && num[index] == '0')
                continue;
            if (path.empty())
            {
                helper(num, index + i, target, num.substr(index, i), res);
            }
            else {
                for (char c : op) {
                    helper(num, index + i, target, path + string(1, c) + num.substr(index, i), res);
                }
            }
        }
    }
};