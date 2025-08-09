class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](auto &a, auto &b) {
            return a[1] < b[1];
        });
        int limit = INT_MIN, count = 0;
        for (auto& interval : intervals) {
            if (interval[0] >= limit) {
                count++;
                limit = interval[1];
            }
        }
        return intervals.size() - count;
    }
};
