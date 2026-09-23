class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int currMax = 0;

        while (l < r) {
            int dist = r - l;

            if (heights[l] < heights[r]) {
                currMax = max(currMax, dist * heights[l]);
                l++;

            } else if (heights[r] < heights[l]) {
                currMax = max(currMax, dist * heights[r]);
                r--;

            } else {
                currMax = max(currMax, dist * heights[r]);
                l++;
                continue;
            }
        }

        return currMax;
    }
};
