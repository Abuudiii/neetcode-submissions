class Solution {
public:
    int maxArea(vector<int>& heights) {
        int currMax = 0;
        int l = 0;
        int r = heights.size() - 1;

        while (l < r) {
            int distance = r - l;
            int minHeight = min(heights[l], heights[r]);
            currMax = max(currMax, minHeight * distance);

            if (heights[l] < heights[r]) {
                l++;
                continue;
            } else if (heights[l] > heights[r]) {
                r--;
                continue;
            } else {
                r--;
            }
        } // End While

        return currMax;
    }
};
