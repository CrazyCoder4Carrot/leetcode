/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
    	vector<int> starts, ends;
    	for(auto interval : intervals){
    		starts.push_back(interval.start);
    		ends.push_back(interval.end);
    	}
    	sort(starts.begin(), starts.end());
    	sort(ends.begin(), ends.end());
    	int empty = 0, rooms = 0, available = 0;
    	for(auto start : starts){
    		while(ends[empty] <= start){
    			++empty;
    			++available;
    		}
    		available? --available: ++rooms;
    	}
    	return rooms;
    }
};