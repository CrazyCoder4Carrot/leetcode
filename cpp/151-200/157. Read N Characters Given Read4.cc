// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int count = 0;
        int readcnt = 0;
        while (n > 0 && count < n) {
            readcnt = read4(buf + count);
            if (readcnt == 0)
                break;
            count += readcnt;
        }
        return min(n, count);
    }
};