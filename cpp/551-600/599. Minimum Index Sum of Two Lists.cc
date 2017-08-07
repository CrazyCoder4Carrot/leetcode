class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string , int> dict;
        for(int i = 0; i < list1.size(); i++){
        	dict[list1[i]] = i;
        }
        int minsum = INT_MAX;
        vector<string> res;
        for(int i = 0; i < list2.size(); i++){
        	if(dict.find(list2[i]) == dict.end())
        		continue;
        	int sum = i + dict[list2[i]];
        	if(sum < minsum){
        		res.clear();
        		minsum = sum;
        	}
        	if(sum == minsum)
        		res.push_back(list2[i]);
        }
        return res;
    }
};