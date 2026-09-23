class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int ans{};

        for (int i = 0; i < 32; i++) {
            int tmp1 = (1 << i) & n;

            if (tmp1) {
                ans |= (1 << (31 - i));
            }
        }

        return ans;
    }
};
