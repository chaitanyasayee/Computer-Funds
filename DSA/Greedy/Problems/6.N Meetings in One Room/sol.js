function maxMeetings(start, end, n) {
  let meetings = [];
  for (let i = 0; i < n; i++) {
    meetings.push([end[i], start[i]]);
  }
  meetings.sort((a, b) => a[0] - b[0]);

  let count = 1;
  let last_end = meetings[0][0];

  for (let i = 1; i < n; i++) {
    if (meetings[i][1] > last_end) {
      count++;
      last_end = meetings[i][0];
    }
  }
  return count;
}
