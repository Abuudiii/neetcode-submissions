class Solution {
public:
    int hammingWeight(uint32_t n) {
        int numOnes{};
 
        while(n) {
            numOnes += n & 1;
            n >>= 1;
        }
        return numOnes;
    }
};
