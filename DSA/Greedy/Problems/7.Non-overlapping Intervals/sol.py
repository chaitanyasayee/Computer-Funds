class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])
        limit = float('-inf')
        count = 0
        for start, end in intervals:
            if start >= limit:
                count += 1
                limit = end
        return len(intervals) - count
