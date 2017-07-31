class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty())
            return 0;
        int res = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    bfs(grid, i, j);
                    res ++;
                }
            }
        }
        return res;
    }
    void bfs(vector<vector<char>> &grid, int i, int j) {
        if (i < 0 || i >= grid.size())
            return;
        if (j < 0 || j >= grid[0].size())
            return;
        queue<pair<int, int>> q;
        q.push(make_pair(i, j));
        while (!q.empty()) {
            pair<int, int> p = q.front();
            q.pop();
            int x = p.first, y = p.second;
            if(x < 0 || x >= grid.size() || y < 0 || y >= grid[0].size() || grid[x][y] == '0')
            	continue;
            grid[x][y] = '0';
            q.push(make_pair(x - 1, y));
            q.push(make_pair(x + 1, y));
            q.push(make_pair(x, y + 1));
            q.push(make_pair(x, y - 1));
        }
    }
};