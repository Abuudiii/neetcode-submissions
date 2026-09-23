#include <array>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> fingerprint;
        vector<vector<string>> ans;
        
        for (const auto& word : strs) {
            array<int, 26> count{};

            for (const auto c : word) {
                count[c - 'a'] += 1;
            }

            fingerprint[count].push_back(word);
        }

        for (const auto& [k, value] : fingerprint) {
            ans.push_back(value);
        }
        
        return ans;
    }
};
