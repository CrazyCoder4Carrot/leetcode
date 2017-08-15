class Solution {
public:
    void reverseWords(string &s) {
        int i = 0, j = 0;
        int sz = s.size();
        while(i < sz){
            while(i < sz && s[i] == ' ')
                i++;
            if(i < sz && j > 0)
                s[j++] = ' ';
            int start = j;
            while(i < sz && s[i] != ' ')
                s[j++] = s[i++];
            reverse(s.begin() + start, s.begin() + j);
        }
        s.resize(j);
        reverse(s.begin(), s.end());
    }
};