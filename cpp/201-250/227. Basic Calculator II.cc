class Solution {
public:
    int calculate(string s) {
        int res = 0;
        int cur_res = 0;
        char op = '+';
        for (int pos = s.find_first_not_of(' '); pos < s.size(); pos = s.find_first_not_of(' ', pos)) {
            if (isdigit(s[pos])) {
                int length = 1;
                while (pos + length < s.size() && isdigit(s[pos + length])) {
                    length++;
                }
                int temp = stoi(s.substr(pos, length));
                pos += length;
                switch (op) {
                case '+':
                    cur_res += temp;
                    break;
                case '-':
                    cur_res -= temp;
                    break;
                case '*':
                    cur_res *= temp;
                    break;
                case '/':
                    cur_res /= temp;
                    break;
                }
            }
            else{
                if(s[pos] == '+' || s[pos] == '-'){
                    res += cur_res;
                    cur_res = 0;
                }
                op = s[pos++];
            }
        }
        return res + cur_res;
    }
};