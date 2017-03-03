class Solution {
public:
    vector<string> generateParenthesis(int n) {
    	vector<string> res;
    	helper("", res, n, n);
    	return res;
    }
    void helper(string path, vector<string> res, int left, int right)
    {
        if(left == 0 && right == 0)
        {
        	res.push_back(path);
        	return
        }
        if(left > 0)
        	helper(path + "(", res, left - 1, right);
        if(right > left)
        	helper(path + ")", res, left, right - 1);
    }
};