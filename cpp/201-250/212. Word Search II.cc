struct Node {
    char c;
    unordered_map<char, Node*> dict;
    Node(char c): c(c) {
        end = false;
    };
    bool end;
    int index;
};
class Solution {
private:
    Node *root;
    vector<string> res;
    vector<Node *> ptrs;
public:
    Solution() {
        root = new Node('#');
        ptrs.push_back(root);
    }
    ~Solution() {
        for (auto ptr : ptrs)
            delete ptr;
    }
    void add(string word, int i) {
        auto node = root;
        for (auto c : word) {
            if (node->dict.find(c) == node->dict.end()) {
                node->dict[c] = new Node(c);
                ptrs.push_back(node->dict[c]);
            }
            node = node->dict[c];
        }
        node->end = true;
        node->index = i;
    }
    void dfs(int i , int j, vector<vector<char>> &board, Node *node, vector<string> &words) {
        if (i < 0 || j < 0 || i >= board.size() || j >= board[i].size())
            return;
        char tmp = board[i][j];
        if(node->dict.find(tmp) == node->dict.end())
            return;
        node = node->dict[tmp];
        if (node->end) {
            node->end = false;
            res.push_back(words[node->index]);
        }
        board[i][j] = '*';
        vector<int> dirs = {0, 1, 0, -1, 0};
        for (int k = 0; k < 4; k++) {
            dfs(i + dirs[k], j + dirs[k + 1], board, node, words);
        }
        board[i][j] = tmp;
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        for (int i = 0; i < words.size(); i++) {
            add(words[i], i);
        }
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                dfs(i, j, board, root, words);
            }
        }
        return res;
    }
};