class Solution {
public:
	int maximalRectangle(vector<vector<char>>& matrix) {
		int m = matrix.size();
		if (m == 0)
			return 0;
		int n = matrix[0].size();
		vector<int> heights(n, 0);
		int res = 0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (matrix[i][j] == '0')
					heights[j] = 0;
				else
					heights[j]++;
			}
			res = max(res, maxhistogram(heights));
		}
		return res;
	}
	int maxhistogram(vector<int> heights){
		stack<int> st;
		heights.push_back(0);
		int res = 0;
		for(int i = 0; i < heights.size(); i++){
			if(st.empty() || heights[st.top()] < heights[i])
				st.push(i);
			else{
				while(!st.empty() && heights[st.top()] >= heights[i]){
					int h = heights[st.top()];
					st.pop();
					int w = st.empty()? i: (i - st.top() - 1);
					res = max(res, w * h);
				}
				st.push(i);
			}
		}
		return res;
	}
};