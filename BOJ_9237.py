firstline = int(input())
s = list(map(int,input().split(" ")))
s.sort(reverse = True)
result = []
for i,j in enumerate(s):
    result.append(i + j + 2)
print(max(result))
