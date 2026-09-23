class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int answer = 0;

        for (const auto x : nums) {
            answer = answer ^ x;
        }

        return answer;
    }
};
