class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count{};

        for (int i = 0; i < 32; i++) {
            int tmp = (1 << i) & n;

            if (tmp) {
                count++;
            }
        }

        return count;
    }
};
