int findPlatform(int arr[], int dep[], int n) {
    sort(arr, arr + n);
    sort(dep, dep + n);

    int plat_needed = 0, max_platforms = 0;
    int i = 0, j = 0;

    while (i < n) {
        if (arr[i] <= dep[j]) {
            plat_needed++;
            max_platforms = max(max_platforms, plat_needed);
            i++;
        } else {
            plat_needed--;
            j++;
        }
    }
    return max_platforms;
}