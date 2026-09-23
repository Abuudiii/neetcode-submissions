
/*
    - for each n, we count the num of ones it contains
    - after n is exhausted, append that count to res
    - repeat for all ns
*/
class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> res;

        for (int i = 0; i <= n; i++) {
            int ones{};
            int x = i;

            while (x) {
                ones++;
                x &= (x - 1);
            }

            res.push_back(ones);
        }

        return res;
    }
};
