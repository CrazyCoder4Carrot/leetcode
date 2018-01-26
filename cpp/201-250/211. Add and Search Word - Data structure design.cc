#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;
struct Node {
    char c;
    unordered_map<char, Node*> dict;
    Node(char c): c(c) {};
};
class WordDictionary {
private:
    Node *root;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new Node('#');
    }

    /** Adds a word into the data structure. */
    void addWord(string word) {
        auto node = root;
        for (auto c : word) {
            if (node->dict.find(c) == node->dict.end()) {
                node->dict[c] = new Node(c);
            }
            node = node->dict[c];
        }
        node->dict['#'] = nullptr;
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to
    represent any one letter. */
    bool dfs(Node *node, string word) {
        bool res = false;
        if(!node)
            return false;
        if (word.empty()){
            return node->dict.find('#') != node->dict.end();
        }
        if (word[0] == '.') {
            for (auto p : node->dict) {
                res |= dfs(p.second, word.substr(1));
            }
        }
        else {
            if (node->dict.find(word[0]) == node->dict.end())
                return false;
            return dfs(node->dict[word[0]], word.substr(1));
        }
        return res;
    }
    bool search(string word) {
        return dfs(root, word);
    }
};


int main() {
    auto wd = WordDictionary();
    wd.addWord("at");
    wd.addWord("and");
    wd.addWord("an");
    wd.addWord("add");
    wd.addWord("bat");
    cout << wd.search("at") << endl;
    cout << wd.search(".") << endl;
    return 0;
}