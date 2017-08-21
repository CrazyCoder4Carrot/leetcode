
class TwoSum {
private:
    unordered_map<int, int> dict;
public:
    /** Initialize your data structure here. */
    TwoSum() {
    }

    /** Add the number to an internal data structure.. */
    void add(int number) {
        dict[number]++;
    }

    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        for (auto it : dict) {
        	int tmp = value - it.first;
        	if(tmp != it.first & dict.count(tmp)){
        		return true;
        	}
        	if(tmp == it.first & it.second >= 2)
        		return true;
        }
        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * bool param_2 = obj.find(value);
 */