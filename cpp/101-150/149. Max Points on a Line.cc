/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
private:
    int gcd(int a, int b) {
        while (b) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }
public:
    int maxPoints(vector<Point>& points) {
        if (points.empty())
            return 0;
        if (points.size() == 1)
            return 1;
        int res = 0;
        for (int i = 0; i < points.size(); i++) {
            int overlap = 0, curmax = 0;
            unordered_map<pair<int, int>, int> k_count;
            for (int j = i + 1; j < points.size(); j++) {
                int dx = points[j].x - points[i].x;
                int dy = points[j].y - points[i].y;
                if (dx == 0 && dy == 0) {
                    overlap++;
                    continue;
                }
                int dvs = gcd(dx, dy);
                pair<int, int> k = make_pair(dx / dvs, dy / dvs);
                if (k_count.find(k) == k_count.end()) {
                    k_count[k] = 1;
                }
                else
                    k_count[k]++;
                curmax = max(curmax, k_count[k]);
            }
            res = max(res, curmax + overlap + 1);
        }
        return res;
    }
};