class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> numCount;
        vector<vector<int>> freq(nums.size() + 1);

        // Builds out numCount map
        for (const auto x : nums) {
            numCount[x]++;
        }

        for (const auto& x : numCount) {
            freq[x.second].push_back(x.first);
        }

        vector<int> result;

        for (int i = freq.size() - 1; i >= 0; i--) {

            for (auto num : freq[i]){
                result.push_back(num);
            }

            if (result.size() == k) {
                return result;
            }
        }   

    }
};
