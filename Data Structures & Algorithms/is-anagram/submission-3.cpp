class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> countS;
        unordered_map<char, int> countT;

        for (int i = 0; i < s.size(); i++) {
            countS[s[i]] += 1;
            countT[t[i]] += 1;
        }

        if (countS == countT) {
            return true;
        }

        return false;
    }
};
