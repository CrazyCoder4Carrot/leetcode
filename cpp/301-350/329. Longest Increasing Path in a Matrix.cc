class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int res = 0;
        if(matrix.empty())
        	return res;
        vector<vector<int>> visited(matrix.size(), vector<int>(matrix[0].size(), 0));
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                res = max(res, dfs(i, j, INT_MIN, 0, res, matrix, visited));
            }
        }
        return res;
    }
    int dfs(int i, int j, int lastval, int length, int &res, vector<vector<int>> &matrix, vector<vector<int>> &visited) {
        if (i < 0 || j < 0 || i >= matrix.size() || j >= matrix[0].size() || matrix[i][j] <= lastval) {
            return 0;
        }
        if(visited[i][j])
        	return visited[i][j];
        int pos[] = {0, 1, 0, -1, 0};
        int maxval = 0;
        for (int k = 0; k < 4; k++) {
            int x = i + pos[k];
            int y = j + pos[k + 1];
            maxval = max(maxval, dfs(x, y, matrix[i][j], length + 1, res, matrix, visited));
        }
        visited[i][j] = maxval + 1;
        return visited[i][j];
    }
};