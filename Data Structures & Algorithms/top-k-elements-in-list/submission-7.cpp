class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        vector<vector<int>> freq(nums.size() + 1);

        for (const auto x : nums) {
            count[x] += 1;
        }

        for (const auto& [k, v] : count) {
            freq[v].push_back(k);
        }

        vector<int> res;
        for (int i = freq.size() - 1; i > 0; i--) {
            for (const auto num : freq[i]) {
                res.push_back(num);

                if (res.size() == k) {
                    return res;
                }
            }
        }
    }
};
