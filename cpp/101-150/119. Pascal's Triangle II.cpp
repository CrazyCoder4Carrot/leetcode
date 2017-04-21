class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res;
        if(rowIndex == 0){
        	vector<int> res(1,1);
        	return res;
        }
        if(rowIndex == 1){
        	vector<int> res(2, 1);
        	return res;
        }
        vector<int> prev(2,1);
        for(int i = 2; i <= rowIndex; i++){
        	vector<int> cur(i + 1, 1);
        	for(int j = 1; j < i; j++){
        		cur[j] = prev[j-1] + prev[j];
        	}
        	swap(cur, prev);
        }
        return prev;
    }
};