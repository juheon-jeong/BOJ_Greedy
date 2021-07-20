testcase = int(input())

list = []
for i in range(testcase):
    list.append(int(input()))


list.sort(reverse=True)

for i in range(len(list)):
    list[i] = list[i] * (i + 1)

print(max(list))