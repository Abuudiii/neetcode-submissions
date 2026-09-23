class Solution {
public:
    int hammingWeight(uint32_t n) {
        int numOnes{};
 
        while(n) {
            int val = n & 1;
            n >>= 1;
            numOnes += val;
        }
        return numOnes;
    }
};
