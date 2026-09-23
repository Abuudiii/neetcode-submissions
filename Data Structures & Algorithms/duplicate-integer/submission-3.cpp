class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seen;

        for (const int x : nums) {
            if (seen.count(x)) {
                return true;
            }

            seen.insert(x);
        }

        return false;
    }
};