testcase = int(input())

words = []
for i in range(testcase):
    words.append(input())

alphabet =[0 for i in range(26)]

for word in words:
    i = 0
    while word:
        now = word[-1]
        alphabet[ord(now) - ord('A')] += pow(10, i)
        i += 1
        word = word[:-1]

alphabet.sort(reverse=True)
answer = 0
for i in range(9, 0, -1):
    answer += i * alphabet[9 - i]
print(answer)
