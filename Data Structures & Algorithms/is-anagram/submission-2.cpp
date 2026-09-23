class Solution {
public:
    bool isAnagram(string s, string t) {
        // Different size == not anagram
        if (s.size() != t.size()) {
            return false;
        }

        // Maps to store count of each string
        unordered_map<char, int> countS;
        unordered_map<char, int> countT;

        // Since size is same, we can iterate over one 
        for (int i = 0; i < s.size(); i++) {
            countS[s[i]]++;
            countT[t[i]]++;
        }

        return countS == countT;

    }
};
