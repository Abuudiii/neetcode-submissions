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

            for (int j = 0; j < 32; j++) {
                int tmp = (1 << j) & i;

                if (tmp) {
                    count++;
                }
            }

            res.push_back(count);
        }

        return res;
    }
};
