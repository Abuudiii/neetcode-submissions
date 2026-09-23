class Solution {
public:
    int maxArea(vector<int>& heights) {
        int currMax = 0;
        int l = 0;
        int r = heights.size() - 1;

        while (l < r) {
            int dist = r - l;

            if (heights[l] < heights[r]) {
                currMax = max(currMax, (heights[l] * dist));
                l++;
                continue;

            } else if (heights[r] < heights[l]) {
                currMax = max(currMax, (heights[r] * dist));
                r--;
                continue;

            } else {
                currMax = max(currMax, (heights[l] * dist));
                l++;
            }
        }

        return currMax;
    }
};
