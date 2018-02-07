class Solution {
public:
    int shortestWordDistance(vector<string>& words, string word1, string word2) {
        int res = words.size();
        int pos1 = -res, pos2 = -res;
        for(int i = 0; i < words.size(); i++){
            if(words[i] == word1){
                if(word1 == word2)
                    pos2 = pos1;
                res = min(res, abs(i - pos2));
                pos1 = i;
            }
            else if(words[i] == word2){
                res = min(res, abs(pos1 - i));
                pos2 = i;
            }
        }
        return res;
    }
};