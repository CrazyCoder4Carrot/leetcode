class Solution {
public:
    char lowcase(char in) {
        if (in <= 'Z' && in >= 'A')
            return in - ('Z' - 'z');
        return in;
    }
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;
        if (s.empty())
            return true;
        while (left <= right) {
            if (!isalpha(s[left]) && !isdigit(s[left])) {
                left ++;
                continue;
            }
            if (!isalpha(s[left]) && !isdigit(s[left])) {
                right--;
                continue;
            }
            if (s[left] == s[right] || lowcase(s[left]) == lowcase(s[right])) {
                left++;
                right--;
            }
            else
                break;
        }
        return left > right;
    }
};