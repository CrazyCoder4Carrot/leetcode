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
	bool static sortfun(const Interval &interval1, const Interval &interval2) {
		return interval1.start < interval2.start;
	}
	vector<Interval> merge(vector<Interval>& intervals) {
		vector<Interval> res;
		sort(intervals.begin(), intervals.end(), sortfun);
		if(intervals.empty())
			return res;
		int j = -1;
		for(int i = 0; i < intervals.size(); i++){
			if(!res.empty() && res[j].end >= intervals[i].start)
				res[j].end = max(intervals[i].end, res[j].end);
			else{
				res.push_back(intervals[i]);
				j++;
			}
		}
		return res;
	}
};