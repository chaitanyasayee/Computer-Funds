def max_students_with_cookies(students, cookies):
    students.sort()
    cookies.sort()
    

    i = j = 0
    count = 0

    while i < len(students) and j < len(cookies):
        if cookies[j] >= students[i]:
            count += 1
            i += 1
        j += 1

    return count
