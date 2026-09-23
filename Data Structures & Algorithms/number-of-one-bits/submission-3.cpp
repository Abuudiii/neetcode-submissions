class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ones{};

        for (int i = 0; i < 32; i++) {
            uint32_t ans = (1 << i);
            if (ans & n) {
                ones++;
            } 
        }

        return ones;
    }
};
