class Solution
{
public:
        int myAtoi(string str)
        {
                long long res = 0;
                int flag = 1;
                if (str == "")
                        return res;
                for (int i = 0; i < str.length(); i++)
                {
                        i = str.find_first_not_of(' ');
                        if (str[i] == '-' || str[i] == '+')
                                flag = (str[i++] == '-') ? -1 : 1;
                        while (str[i] >= '0' && str[i] <= '9')
                        {
                                res = res * 10 + (str[i++] - '0');
                                if (res * flag < INT_MIN)
                                        return INT_MIN;
                                if (res * flag > INT_MAX)
                                        return INT_MAX;
                        }
                        return res * flag;
                }

        }
};