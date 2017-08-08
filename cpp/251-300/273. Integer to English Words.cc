class Solution {
public:
    string numberToWords(int num) {
        string nums[] = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        string numtens[] = {"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        if (num < 20)
            return nums[num];
        map<int, string> dict;
        dict[100] = "Hundred";
        dict[1000] = "Thousand";
        dict[1000000] = "Million";
        dict[1000000000] = "Billion";
        std::vector<string> res;
        long arr[] = {100, 1000, 1000000, 1000000000};
        for (int i = 3; i >= 0 ; i--) {
            if (num >= arr[i]) {
                res.push_back(numberToWords(num/ arr[i]));
                res.push_back(dict[arr[i]]);
                num = num % arr[i];
            }
        }
        for (int i = 9; i >= 2 ; i--) {
            if (num >= i * 10) {
                res.push_back(numtens[i - 2]);
                num = num % (i * 10);
            }
        }
        if (num)
            res.push_back(nums[num]);
        string resstr = "";
        if(!res.empty())
            resstr = res[0];
        for(int i = 1; i < res.size(); i++)
            resstr = resstr + " " + res[i];
        return resstr;
    }
};