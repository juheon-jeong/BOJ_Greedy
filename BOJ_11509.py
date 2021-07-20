tc = int(input())
pose = list(map(int, input().split(" ")))

check = [0] * 1000001

result = 0

for i in range(len(pose)):
    if check[pose[i]] == 0:
        result += 1
        check[pose[i] - 1] += 1

    else:
        check[pose[i]] -= 1
        check[pose[i] - 1] += 1

print(result)


