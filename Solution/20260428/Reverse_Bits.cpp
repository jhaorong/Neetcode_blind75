// Bit Manipulation
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        for (int i = 0; i < 32; i++) {
            uint32_t bit = (n >> i) & 1;
            res |= (bit << (31 - i));
        }
        return res;
    }
};

// Bit Manipulation (Optimal)
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        // if n = 43261596
        uint32_t ret = n; // n in binary is 0000 0010 1001 0100 0001 1110 1001 1100
        ret = (ret >> 16) | (ret << 16); // 0001 1110 1001 1100 | 0000 0010 1001 0100
        ret = ((ret & 0xff00ff00) >> 8) | ((ret & 0x00ff00ff) << 8); // 1001 1100 | 0001 1110 | 1001 0100 | 0000 0010
        ret = ((ret & 0xf0f0f0f0) >> 4) | ((ret & 0x0f0f0f0f) << 4); // 1100 | 1001 | 1110 | 0001 | 0100 | 1001 | 0010 | 0000
        ret = ((ret & 0xcccccccc) >> 2) | ((ret & 0x33333333) << 2); // 00 | 11 | 01 | 10 | 10 | 11 | 01 | 00 | 00 | 01 | 01 | 10 | 10 | 00 | 00 | 00
        ret = ((ret & 0xaaaaaaaa) >> 1) | ((ret & 0x55555555) << 1); // 0011 1001 0111 1000 0010 1001 0100 0000
        return ret;
    }
};