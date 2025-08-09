import java.util.*;

class Meeting {
    int start, end;

    Meeting(int s, int e) {
        start = s;
        end = e;
    }
}

class Solution {
    public int maxMeetings(int[] start, int[] end, int n) {
        Meeting[] meetings = new Meeting[n];
        for (int i = 0; i < n; i++) {
            meetings[i] = new Meeting(start[i], end[i]);
        }

        Arrays.sort(meetings, (a, b) -> a.end - b.end);

        int count = 1, last_end = meetings[0].end;
        for (int i = 1; i < n; i++) {
            if (meetings[i].start > last_end) {
                count++;
                last_end = meetings[i].end;
            }
        }
        return count;
    }
}
