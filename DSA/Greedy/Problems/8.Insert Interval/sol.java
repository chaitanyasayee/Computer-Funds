import java.util.*;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new ArrayList<>();
        int i = 0, n = intervals.length;

        // Step 1
        while (i < n && intervals[i][1] < newInterval[0])
            res.add(intervals[i++]);

        // Step 2
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
            i++;
        }
        res.add(newInterval);

        // Step 3
        while (i < n)
            res.add(intervals[i++]);

        return res.toArray(new int[res.size()][]);
    }
}
