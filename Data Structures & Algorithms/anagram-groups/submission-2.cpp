class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> anagrams;
        vector<vector<string>> results;

        for (const string& x : strs) {
            vector<int> fingerprint(26);

            for (char c : x) {
                fingerprint[c - 'a']++;
            }

            anagrams[fingerprint].push_back(x);
        }

        for (const auto& pairs : anagrams) {
            results.push_back(pairs.second);
        }

        return results;
    }
};
