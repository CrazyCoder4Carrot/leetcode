class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<unordered_set<int>> graph = make_graph(numCourses, prerequisites);
        vector<bool> onpath(numCourses, false);
        bool res = true;
        for (int i = 0; i < numCourses; i++) {
            if (onpath[i])
                continue;
            vector<bool> visited(numCourses, false);
            bool res = dfs(i, graph, visited, onpath);
            if (!res)
                return false;
        }
        return true;
    }
private:
    vector<unordered_set<int>> make_graph(int numCourses, vector<pair<int, int>> &prerequisites) {
        vector<unordered_set<int>> graph(numCourses);
        for (auto it : prerequisites) {
            graph[it.first].insert(it.second);
        }
        return graph;
    }
    bool dfs(int node, vector<unordered_set<int>> &graph, vector<bool> &visited, vector<bool> &onpath) {
        if (onpath[node])
            return true;
        if (visited[node])
            return false;
        visited[node] = true;
        for (int i : graph[node]) {
            bool res = dfs(i, graph, visited, onpath);
            if (!res)
                return false;
        }
        onpath[node] = true;
        return true;
    }
};