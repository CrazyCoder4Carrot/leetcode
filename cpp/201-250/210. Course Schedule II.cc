class Solution {
private:
    vector<int> res;
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        if (numCourses == 0)
            return res;
        vector<bool> onpath(numCourses, false);
        vector<unordered_set<int>> graph = make_graph(numCourses, prerequisites);
        bool nocycle;
        for (int i = 0; i < numCourses; i++) {
            vector<bool> visited(numCourses, false);
            nocycle = dfs(i, graph, visited, onpath);
            if (!nocycle){
                res.erase(res.begin(), res.end());
                return res;
            }
        }
        return res;
    }
    vector<unordered_set<int>> make_graph(int numCourses, vector<pair<int, int>>& prerequisites) {
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
        res.push_back(node);
        onpath[node] = true;
        return true;
    }
};