N = int(input())
M = int(input())

ps = list(map(int, input().split(" ")))

count = 0

for i in range(N):
    s = M - ps[i]
    if s in ps:
        count += 1

print(int(count / 2))