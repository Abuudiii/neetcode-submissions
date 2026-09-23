class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            int a = nums[i];

            if (a > 0) {
                break;
            }

            if (i > 0 && (a == nums[i - 1])) {
                continue;
            }

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int currSum = a + nums[l] + nums[r];

                if (currSum < 0) {
                    l++;
                    continue;

                } else if (currSum > 0) {
                    r--;
                    continue;

                } else {
                    result.push_back({a, nums[l], nums[r]});
                    l++;
                    r--;

                    while (l < r && (nums[l] == nums[l - 1])) {
                        l++;
                    }
                }
            }
        } // End of for lopp

        return result;
    }
};
