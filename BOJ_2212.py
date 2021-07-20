sensor = int(input())

center = int(input())

purpose = input().split(" ")

for i in range(len(purpose)):
    purpose[i] = int(purpose[i])

purpose.sort()
dist = []
print(sum(dist))

if center >= sensor:
    print(0)
    exit()
else:
    temp = purpose[0]
    for i in range(1, len(purpose)):
        dist.append(purpose[i] - temp)
        temp = purpose[i]
    dist.sort(reverse=True)
    for i in range(center - 1):
        dist.pop(0)
print(sum(dist))