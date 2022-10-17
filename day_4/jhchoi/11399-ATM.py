import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
p = sorted(list(map(int, input().split()))) # 돈 인출하는 시간 적은 순으로 정렬
result = 0

# 각 사람의 돈 인출하는데 걸리는 총 시간
for i in range(1, n+1):
    result += sum(p[:i])

print(result)