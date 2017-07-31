class Solution {
public:
    int Find(int index, vector<int> &nodes) {
        if (nodes[index] < 0)
            return index;
        int root = Find(nodes[index], nodes);
        nodes[index] = root;
        return root;
    }
    void Union(int i, int j, vector<int> &nodes) {
        int root1 = Find(i, nodes);
        int root2 = Find(j, nodes);
        if (root1 == root2)
            return;
        if (nodes[root2] < nodes[root1]) {
            nodes[root2] += nodes[root1];
            nodes[root1] = root2;
        }
        else {
            nodes[root1] += nodes[root2];
            nodes[root2] = root1;
        }
    }
    vector<int> numIslands2(int m, int n, vector<pair<int, int>>& positions) {
        vector<int> v(m * n, -1);
        vector<bool> land(n * m , false);
        vector<int> res;
        if (positions.empty())
            return res;
        for (auto p : positions) {
            int val = 1;
            int x = p.first, y = p.second;
            land[x * n + y] = true;
            vector<pair<int, int>> nbs;
            nbs.push_back(make_pair(x - 1, y));
            nbs.push_back(make_pair(x + 1, y));
            nbs.push_back(make_pair(x, y - 1));
            nbs.push_back(make_pair(x, y + 1));
            for (auto nb : nbs) {
                int nx = nb.first, ny = nb.second;
                if (nx < 0 || nx >= m || ny < 0 || ny >= n || !land[nx * n + ny])
                    continue;
                if (Find(x * n + y, v) != Find(nx * n + ny, v)) {
                    val--;
                    Union(x * n + y, nx * n + ny, v);
                }
            }
            if (res.empty())
                res.push_back(1);
            else
                res.push_back(res.back() + val);
        }
        return res;
    }
};