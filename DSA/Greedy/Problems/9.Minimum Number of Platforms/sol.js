function findPlatform(arr, dep, n) {
  arr.sort((a, b) => a - b);
  dep.sort((a, b) => a - b);

  let plat_needed = 0,
    max_platforms = 0;
  let i = 0,
    j = 0;

  while (i < n) {
    if (arr[i] <= dep[j]) {
      plat_needed++;
      max_platforms = Math.max(max_platforms, plat_needed);
      i++;
    } else {
      plat_needed--;
      j++;
    }
  }

  return max_platforms;
}
