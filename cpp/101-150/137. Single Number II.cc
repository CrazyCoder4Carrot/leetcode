class Solution {
public:
    int singleNumber(vector<int>& nums) {
    	int res = 0;
    	vector<int> bits(32, 0);
    	for(auto num : nums){
    		for(int i = 0; i < 32; i++){
    			if((1<<i) & num)
    				bits[i]++;
    		}
    	}
    	for(int i = 0; i < 32; i++){
    		if(bits[i] % 3 != 0)
    			res = res | (1<<i);
    	}
    	return res;
    }
};