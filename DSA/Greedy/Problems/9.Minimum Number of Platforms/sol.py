def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()
    i = j = 0
    plat_needed = max_platforms = 0

    while i < n:
        if arr[i] <= dep[j]:
            plat_needed += 1
            max_platforms = max(max_platforms, plat_needed)
            i += 1
        else:
            plat_needed -= 1
            j += 1

    return max_platforms