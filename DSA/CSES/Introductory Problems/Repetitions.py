repre = str(input())
ans = 0
flag = 1
temp = 1
for i in range(len(repre)-1):
    if repre[i] == repre[i+1]:
        temp+=1
    else:
        ans = max(ans, temp)
        temp = 1
ans = max(ans, temp)
print(ans)