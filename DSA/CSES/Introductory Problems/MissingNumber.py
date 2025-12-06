n = int(input())
total = (n * (n+1))//2
actual = 0
x = list(map(int, input().split()))
actual = sum(x)
print(abs(total - actual))