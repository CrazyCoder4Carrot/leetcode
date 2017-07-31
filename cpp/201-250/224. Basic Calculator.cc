class Solution {
public:
    int calculate(string s) {
    	if(s.empty())
    		return 0;
    	s = '(' + s + ')';
        stack<string> st;
        int res = 0;
        for (int pos = s.find_first_not_of(" "); pos < s.size(); pos = s.find_first_not_of(" ", pos)) {
            if (s[pos] == '(' || s[pos] == '+' || s[pos] == '-') {
                st.push(string(1, s[pos++]));
                continue;
            }
            if (isdigit(s[pos])) {
                int l = 1;
                while (pos + l < s.size() && isdigit(s[pos + l])) {
                	l++;
                }
                st.push(s.substr(pos, l));
                pos += l;
                continue;
            }
            if(s[pos++] == ')'){
            	std::vector<string> v;
            	while(st.top() != "("){
            		v.push_back(st.top());
            		st.pop();
            	}
            	st.pop();
            	reverse(v.begin(), v.end());
            	st.push(to_string(cal(v)));
            }
        }
        return stoi(st.top());
    }
    int cal(std::vector<string> &v) {
        int res = 0;
        char op = '+';
        for (int i = 0; i < v.size(); i++) {
        	if(v[i] == "+"){
        		op = '+';
        		continue;
        	}
        	if(v[i] == "-"){
        		op = '-';
        		continue;
        	}
        	switch(op){
        		case '+':
        		res += stoi(v[i]);
        		break;
        		case '-':
        		res -= stoi(v[i]);
        		break;
        	}
        }
        return res;
    }
};