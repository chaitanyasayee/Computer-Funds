var eraseOverlapIntervals = function (intervals) {
  intervals.sort((a, b) => a[1] - b[1]);
  let limit = -Infinity,
    count = 0;
  for (let [start, end] of intervals) {
    if (start >= limit) {
      count++;
      limit = end;
    }
  }
  return intervals.length - count;
};
