class Solution:
    def maxMeetings(self, start, end, n):
        meetings = sorted(zip(end, start))
        count = 1
        last_end = meetings[0][0]

        for i in range(1, n):
            if meetings[i][1] > last_end:
                count += 1
                last_end = meetings[i][0]
        return count
