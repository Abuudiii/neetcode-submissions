class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result;
        int l = 0;
        int r = numbers.size() - 1;

        while (l < r) {
            if (numbers[l] + numbers[r] < target) {
                l++;
                continue;

            } else if (numbers[l] + numbers[r] > target) {
                r--;
                continue;

            } else {
                return {l + 1, r + 1};
            }
        }
    }
};
