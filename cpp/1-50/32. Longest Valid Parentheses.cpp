class Solution {
public:
	int longestValidParentheses(string s) {
		stack<int> stack;
		stack.push(-1);
		int res = 0;
		for (int i = 0; i < s.size(); i++) {
			int temp = stack.top();
			if (temp >= 0 && s[i] == ')' && s[temp] == '(') {
			    stack.pop();
				res = max(res, i - stack.top());
			}
			else
				stack.push(i);
		}
		return res;
	}
};