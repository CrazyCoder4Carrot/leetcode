class Solution {
public:
    int evalRPN(vector<string>& tokens) {
    	unordered_map<string, function<int (int, int)>> map = {
    		{"+", [](int a, int b) {return a + b;}},
    		{"-", [](int a, int b) {return a - b;}},
    		{"*", [](int a, int b) {return a * b;}},
    		{"/", [](int a, int b) {return a / b;}}
    	};
        if (tokens.empty())
            return 0;
        stack<int> s;
        for (int i = 0; i < tokens.size(); i++) {
            if(map.find(tokens[i]) == map.end()){
            	s.push(stoi(tokens[i]));
            }
            else {
            	int op2 = s.top();
            	s.pop();
            	int op1 = s.top();
            	s.pop();
                s.push(map[tokens[i]](op1, op2));
            }
        }
        return s.top();
    }
};