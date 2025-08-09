var insert = function (intervals, newInterval) {
  const res = [];
  let i = 0,
    n = intervals.length;

  // Step 1
  while (i < n && intervals[i][1] < newInterval[0]) {
    res.push(intervals[i]);
    i++;
  }

  // Step 2
  while (i < n && intervals[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
    i++;
  }
  res.push(newInterval);

  // Step 3
  while (i < n) res.push(intervals[i++]);

  return res;
};
