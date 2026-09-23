class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> res{};
        res.push_back(0);
        /*
            - 1111
            - 1000
        */

        for (int i = 1; i <= n; i++) {
            int count{};
            int x = i;

            while (x) {
                count += x & 1;
                x >>= 1;
            }

            res.push_back(count);
        }

        return res;
    }
};
