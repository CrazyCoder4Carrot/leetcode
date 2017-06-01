class Solution {
public:
    void dfshelper(string word, vector<vector<string>> &res, vector<string> &path, map<string, bool> &wordDict, string endWord) {
        if (!wordDict[word] || find(path.begin(), path.end(), word) != -1)
            return;
        if (word == endWord) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < word.size(); i++) {
            string newWord = word;
            for (int j = 0; j < 26; j++) {
            	newWord[i] = 'a' + j;
            	if(newWord == word)
            		continue;
                path.push_back(newWord);
                dfshelper(newWord, res, path, wordDict, endWord);
                path.pop_back();
            }
        }
    }
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string >> res;
        map<string, bool> wordDict;
        for (auto word : wordList) {
            wordDict[word] = true;
        }
        vector<string> path;
        for (int i = 0; i < beginWord.size(); i++) {
            string newWord = beginWord;
            for (int j = 0; j < 26; j++) {
            	newWord[i] = 'a' + j;
            	if(newWord == beginWord)
            		continue;
                path.push_back(newWord);
                dfshelper(newWord, res, path, wordDict, endWord);
                path.pop_back();
            }
        }
        return res;
    }

};