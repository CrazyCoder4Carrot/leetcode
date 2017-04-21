class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int>> res;
		if(numRows == 0)
			return res;
		vector<int> row1(1,1);
		res.push_back(row1);
		if(numRows == 1){
			return res;
		}
		vector<int> row2(2,1);
		res.push_back(row2);
		if(numRows == 2){
			return res;
		}
		for(int i = 3; i <= numRows; i++){
			vector<int> row(i, 1);
			for(int j = 1; j < i - 1; j++){
				row[j] = res[i-2][j-1] + res[i-2][j];
			}
			res.push_back(row);
		}
		return res;
	}
};