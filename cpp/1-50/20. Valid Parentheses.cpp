class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        string left = "([{";
        string right = ")]}";
        for(int i = 0; i < s.size(); i++)
        {
            if(left.find(s[i]) != string::npos)
                stack.push_back(s[i]);
            else{
                int index = right.find(s[i]);
                if(!stack.empty() && stack[stack.size() - 1] == left[index])
                    stack.pop_back;
                else
                    return false;
                }
        }
        return stack.empty();
    }
};