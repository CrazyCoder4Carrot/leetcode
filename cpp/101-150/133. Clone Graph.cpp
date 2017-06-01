/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
struct UndirectedGraphNode {
    int label;
    vector<UndirectedGraphNode *> neighbors;
    UndirectedGraphNode(int x) : label(x) {};
};
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (!node)
            return NULL;
        UndirectedGraphNode *copy = new UndirectedGraphNode(node->label);
        mp[node] = copy;
        queue<UndirectedGraphNode *> level;
        level.push(node);
        while (!level.empty()) {
        	UndirectedGraphNode *cur = level.front();
        	level.pop();
            for (auto neighbor : cur->neighbors) {
                if (!mp[neighbor]) {
                    UndirectedGraphNode *nb_copy = new UndirectedGraphNode(neighbor->label);
                    mp[neighbor] = nb_copy;
                    level.push(neighbor);
                }
                mp[cur]->neighbors.push_back(mp[neighbor]);
            }
        }
        return mp[node];
    }
private:
    unordered_map<UndirectedGraphNode *, UndirectedGraphNode *> mp;
};