class Solution {
public:
    int convert(char c) {
        switch (c) {
        case 'A':
            return 0;
            break;
        case 'C':
            return 1;
            break;
        case 'G':
            return 2;
            break;
        case 'T':
            return 3;
        }
        return -1;
    }
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        unordered_map<long, int> num2idx;
        unordered_map<long, int> cnt;
        long tmp = 0;
        for (int i = 0; i < s.size(); i++) {
            tmp = tmp * 4 + convert(s[i]);
            if (i >= 9) {
                if (i >= 10)
                    tmp = tmp & 0xfffff;
                cnt[tmp]++;
                if (cnt[tmp] == 2)
                    res.push_back(s.substr(i - 9, 10));
            }
        }
        return res;
    }
};