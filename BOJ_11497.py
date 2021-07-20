import sys
testcase = int(sys.stdin.readline().rstrip())

for i in range(testcase):
    N = int(sys.stdin.readline().rstrip())
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    info = sorted(info)
    answer = []

    if N % 2:
        for i in range(0, N, 2):
            answer.append(info[i])
        for i in range(N-2, 0, -2):
            answer.append(info[i])
    else:
        for i in range(0, N, 2):
            answer.append(info[i])
        for i in range(N - 1, 0, -2):
            answer.append(info[i])

    result = abs(answer[0] - answer[N - 1])

    for i in range(N - 1):
        result = max(result, abs(answer[i] - answer[i + 1]))
    print(result)