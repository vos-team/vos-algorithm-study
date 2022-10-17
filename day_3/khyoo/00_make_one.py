import sys

getNum = lambda: int(sys.stdin.readline().strip())

n = getNum()
answers = {}
answers[1] = 0
answers[2] = 1
answers[3] = 1

# for i in range(2, x + 1):
#     answers[i] = answers[i - 1] + 1
#     if i % 2 == 0:
#         answers[i] = min(answers[i], answers[i // 2] + 1)
#     if i % 3 == 0:
#         answers[i] = min(answers[i], answers[i // 3] + 1)


def solution(x):
    if x in answers:
        return answers[x]
    else:
        answer = min(1 + solution(x // 2) + x % 2, 1 + solution(x // 3) + x % 3)
        answers[x] = answer
        return answer


solution(n)
print(answers[n])
