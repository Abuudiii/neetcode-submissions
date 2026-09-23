class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;

        for (int i = 0; i < 32; i++) {
            int bit = (1 << i) & n;
            if (bit) {
                count++;
            }
        }

        return count;
    }
};
