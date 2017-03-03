class Solution {
public:
        string intToRoman(int num) {
                string romanstr[13] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
                int romanval[13] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
                string res = "";
                for(int i = 13 - 1; i >= 0 ; i--)
                {
                        while(num >= romanval[i]){
                                num -= romanval[i];
                                res = res + romanstr[i];
                        }
                }
                return res;
        }
};