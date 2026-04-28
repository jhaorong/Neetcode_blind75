// Brute Force
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
public:
    vector<int> countBits(int n) {
        vector<int> count(n+1);
        for(int i=0;i<=n;i++)
        {
            count[i] = hammingWeight(i);
        }
        return count;
    }
};

//DP
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> count(n+1);
        count[0] = 0;
        for(int i=1;i<=n;i++)
        {
            count[i] = count[i/2] + (i & 1);
        }
        return count;
    }
};
