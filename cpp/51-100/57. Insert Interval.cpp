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
	bool static mysort(const Interval &interval1, const  Interval &interval2)
	{
		return interval1.start < interval2.start;
	}
	vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
		intervals.push_back(newInterval);
		vector<Interval> res;
		sort(intervals.begin(), intervals.end(), mysort);
		int j = -1;
		for (int i = 0; i < intervals.size(); i++) {
			if (!res.empty() && res[j].end >= intervals[i].start)
			{
				res[j].end = max(res[j].end, intervals[i].end);
			}
			else
			{
				res.push_back(intervals[i]);
				j++;
			}
		}
		return res;
	}
};