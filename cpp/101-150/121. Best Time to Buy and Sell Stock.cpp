class Solution {
public:
    int maxProfit(vector<int>& prices) {
    	if(prices.size() < 2)
    		return 0;
    	int minval = prices[0];
    	int res = 0;
    	for(int i = 1; i < prices.size(); i++){
    		res = max(res, prices[i] - minval);
    		minval = min(prices[i], minval);
    	}
    	return res;
    }
};