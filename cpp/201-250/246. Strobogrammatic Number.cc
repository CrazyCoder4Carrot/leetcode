class Solution {
public:
    bool isStrobogrammatic(string num) {
        if(num.empty())
            return true;
        int m = num.size();
        if(num.size() % 2 == 1 && (num[m/2] != '8' && num[m/2] != '0' && num[m/2] != '1'))
            return false;
        int i = 0, j = num.size() - 1;
        for(;i < j; i++, j--){
            if(num[i] == '8' && num[j] == '8')
                continue;
            else if(num[i] == '6' && num[j] == '9')
                continue;
            else if(num[i] == '9' && num[j] == '6')
                continue;
            else if(num[i] == '1' && num[j] == '1')
                continue;
            else if(num[i] == '0' && num[j] == '0')
                continue;
            else return false;
        }
        return true;
    }
};