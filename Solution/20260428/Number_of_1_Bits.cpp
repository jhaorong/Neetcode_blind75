class Solution {
public:
    int hammingWeight(uint32_t n) {
        int weight = 0;
        for(int i=0;i<32;i++)
        {
            if(n & 1)
            {
                weight += 1;
            }
            n = n >> 1;
        }
        return weight;
    }
};