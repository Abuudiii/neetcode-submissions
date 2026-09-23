class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int currMax = 0;

        while (l < r) {
            currMax = max(currMax, (min(heights[l], heights[r]) * (r - l)));

            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return currMax;
    }
};
