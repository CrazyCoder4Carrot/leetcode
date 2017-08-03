class Solution {
public:
    string alienOrder(vector<string>& words) {
        if (words.empty())
            return "";
        unordered_map<char, unordered_set<char>> graph = make_graph(words);
        string res = "";
        vector<bool> onpath(26, false);
        for (int i = 0; i < 26; i++) {
            char node = i + 'a';
            if(graph.find(node) == graph.end())
                continue;
            vector<bool> visited(26, false);
            if(!dfs(node, graph, onpath, visited, res))
            	return "";
        }
        return res;
    }
    bool dfs(char node, unordered_map<char, unordered_set<char>> &graph, vector<bool> &onpath, vector<bool> &visited, string &res) {
        cout<<node<<endl;
        if (onpath[node - 'a'])
            return true;
        if (visited[node - 'a'])
            return false;
        visited[node - 'a'] = true;
        for (char c : graph[node]) {
            if(!dfs(c, graph, onpath, visited, res))
            	return false;
        }
        onpath[node - 'a'] = true;
        res = string(1, node) + res;
        return true;
    }
    unordered_map<char, unordered_set<char>> make_graph(vector<string> &words) {
        unordered_map<char, unordered_set<char>> graph;
        for(auto word: words){
        	for(auto c : word)
        		graph[c] = {};
        }
        for (int i = 0; i < words.size(); i++) {
            if (i < words.size() - 1) {
                string cur = words[i];
                string next = words[i + 1];
                for (int j = 0; j < cur.size() && j < next.size(); j++) {
                    if (cur[j] != next[j]) {
                        graph[cur[j]].insert(next[j]);
                        break;
                    }
                }
            }
        }
        return graph;
    }
};