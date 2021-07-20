N = int(input())
purpose = list(map(int, input().split(" ")))

three = 4
two = 8 * N - 12
one = 5 * pow(N, 2) - 16 * N + 12

p1 = []
p2 = []
p3 = []

p1.append(purpose[0])
p1.append(purpose[5])

p2.append(purpose[1])
p2.append(purpose[4])

p3.append(purpose[2])
p3.append(purpose[3])

temp1 = min(p1) + min(p2) + min(p3)
temp2 = min(min(p1) + min(p2), min(p2) + min(p3), min(p1) + min(p3))
temp3 = min(min(p1), min(p2), min(p3))

result = temp1 * three + temp2 * two + temp3 * one

if N == 1:
    sorted(purpose)
    purpose.remove(max(purpose))
    print(sum(purpose))
else:
    print(result)

