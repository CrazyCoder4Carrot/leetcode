// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {

    int readPos = 0, writePos = 0;
    char buff[4];
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        for (int i = 0; i < n; i++) {
            if (readPos == writePos) {
                writePos = read4(buff);
                readPos = 0;
                if (writePos == 0)
                    return i;
            }
            buf[i] = buff[readPos++];
        }
        return n;
    }
};