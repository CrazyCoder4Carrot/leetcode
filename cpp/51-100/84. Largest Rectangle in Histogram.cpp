class Solution {
public:
	int largestRectangleArea(vector<int>& heights) {
		stack<int> st;
		heights.push_back(0);
		int n = heights.size();
		int res = 0;
		int h, w;
		for(int i = 0; i < n; i++){
			if(st.empty() || heights[st.top()] < heights[i])
				st.push(i);
			else{
				while(!st.empty() && heights[i] <= heights[st.top()]){
					h = heights[st.top()];
					st.pop();
					w = st.empty()? i: (i - st.top() - 1);
					res = max(res, h * w);
				}
				st.push(i);
			}
		}
		return res;
	}
};